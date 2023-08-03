import os
import sys

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import json
import numpy as np
import reverse_geocode
import requests
from bs4 import BeautifulSoup
import pickle
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import math
from population.relevant_data.scraping import *

############################################################
# SUPPORT FOR INITIALIZING STRUCTURE FROM GEOMETRIC OBJECT #
############################################################

def create_tile_dictionary(json_object):
    """
    Given a json object of the form found in geometry/geometries, returns a python dictionary of the tile centers.
    """
    tiles = json_object['features']
    tile_dictionary = {}
    counter = 0
    for tile in tiles:

        # Find center of each tile
        coordinates = tile['geometry']['coordinates'][0]
        bottom_left, top_left, top_right = coordinates[0], coordinates[1], coordinates[2]
        mid_left = (bottom_left[0], (bottom_left[1] + top_left[1])/2)
        mid_top = ((top_left[0] + top_right[0])/2, top_left[1])
        center = (mid_left[0], mid_top[1])

        # Populate dictionary
        tile_dictionary[counter] = center
        counter += 1        

    return tile_dictionary

##################### 
# TILE ORGANIZATION #
#####################

def create_prefecture_tile_dict(prefecture_city_dictionary, tile_dictionary):
    """
    Given prefecture_city_dictionary returned by parse_scraped_info() and a tile dictionary,
    creates a dictionary with prefectures as keys and tiles as values.
    """

    # Organize by city
    city_list = []
    city_dict = {}
    prefecture_tile_dict = {}
    for prefecture, list in prefecture_city_dictionary.items():
        city_list += list
        prefecture_tile_dict[prefecture] = []
    
    for i, coordinates in tile_dictionary.items():
        nearest_city = None
        min_dist = 100000
        for city in city_list:
            city, str_coords = city[0], city[1]
            try:
                city_coords = [float(str_coords[1]), float(str_coords[0])]
            except:
                continue

            dist = math.sqrt((coordinates[0] - city_coords[0])**2 + (coordinates[1] - city_coords[1])**2)
            if dist < min_dist:
                min_dist = dist
                nearest_city = city
        
        if nearest_city not in city_dict:
            city_dict[nearest_city] = [i]
        else:
            city_dict[nearest_city].append(i)
    
    for prefecture, cities in prefecture_city_dictionary.items():
        for city in cities:
            try:
                prefecture_tile_dict[prefecture] += city_dict[city[0]]
            except:
                continue

    change_key(prefecture_tile_dict, 'Hyōgo', 'Hyogo')
    change_key(prefecture_tile_dict, 'Kōchi', 'Kochi')
    change_key(prefecture_tile_dict, 'Ōita', 'Oita')

    return prefecture_tile_dict

#######################################
# SUPPORT FOR POPULATION DISTRIBUTION #
#######################################

def generateDistribution(prefecture_tile_dict, prefecture_pop_dict, prefecture_area_dict):
    """
    Given a tile dictionary, and two dicts of the form returned by prefecture data,
    returns a dictionary with tile indices as keys and pdf values as values
    """
    tile_pdf_dict = {}
    for prefecture, tiles in prefecture_tile_dict.items():
        area = len(tiles)
        for tile in tiles:
            tile_pdf_dict[tile] = round(prefecture_pop_dict[prefecture] / area , 7)

    return tile_pdf_dict

def normalizeDistribution(tile_pdf_dict):
    """
    Given a tile_pdf_dict of the form returned by generateDistribution, normalizes so the sum of each
    tiles value is 1. Returns a new dictionary with the normalized values. Does not modify orginal
    """
    normalized_dict = {}
    normalizing_constant = 1/sum(tile_pdf_dict.values())
    for key,val in tile_pdf_dict.items():
        normalized_dict[key] = round(val * normalizing_constant, 5)
        
    return normalized_dict

if __name__ == '__main__':

    # Forcing path to be parent directory
    os.chdir(parent_dir)

    # Load relevant data
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)

    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as file:
        data_dict = pickle.load(file)
        prefecture_tile_dict = data_dict['prefecture_tile_dict']
        prefecture_pop_dict = data_dict['prefecture_pop_dict']
        prefecture_area_dict = data_dict['prefecture_area_dict']

    # Normalize pdf
    tile_dictionary = create_tile_dictionary(json_object)
    distribution = generateDistribution(prefecture_tile_dict, prefecture_pop_dict, prefecture_area_dict)
    normalized = normalizeDistribution(distribution)
    print(normalized)

        

