
import json
import numpy as np
import data_visualization as dv
import reverse_geocode
import requests
from bs4 import BeautifulSoup
import pickle
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import math

##############################
# RAW JSON DATA MANIPULATION #
##############################

def create_python_object(json_object):
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

################
# WEB SCRAPING #
################

def prefecture_data():
    """
    Returnns a dictionary with prefectures as keys and a list of cities as values corresponding to the cities
    contained in that prefecture
    """
    # Retrieve content
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Japan"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # Initialize container list and scrape html content
    container_list = []
    for table in soup.findAll('table'):
        if table.get('class') == ['wikitable', 'sortable']:
            tbody = table.find('tbody')
            for tr in tbody.findAll('tr'):
                td_element = tr.findAll('td')
                parsed = []
                for elt in td_element:
                    a_element = elt.find('a')
                    if a_element:
                        title = a_element.get('title')
                        href = a_element.get('href')
                        if title:
                            parsed.append(title)
                            if 'Prefecture' in title:
                                continue
                            else:
                                new_url = "https://en.wikipedia.org" + href
                                response = requests.get(new_url)
                                new_content = response.content
                                lat_lon_soup = BeautifulSoup(new_content, "html.parser")
                                div = lat_lon_soup.find('div', {'class' :'vector-body-before-content'})
                                span = div.find('span', {'class': 'geo'})
                                if span != None:
                                    lat_lon = span.text.replace(' ', '')
                                    parsed.append(lat_lon.split(';'))

                if parsed != None:
                    container_list.append(parsed)
            break

    with open('./population/prefecturedata.json', 'w') as f:
        f.write(json.dumps(container_list, indent = 2))

def parse_scraped_info():
    """
    Reads from prefecturedata.json to create a python dictionary containing relevant information
    """
    with open('./population/data.pkl', 'rb') as file:
        data_list = pickle.load(file)
    
    prefecture_dict = {}
    for elt in data_list:
        if len(elt) < 3:
            continue
        city, coords, prefecture = elt[0], elt[1], elt[2]
        if ',' in city:
            city = city.split(',')[0]
        if 'Prefecture' in prefecture:
            prefecture = prefecture.split(' ')[0]

        if type(prefecture) == str:
            if prefecture in prefecture_dict:
                prefecture_dict[prefecture].append([city, coords])
            else:
                prefecture_dict[prefecture] = [city, coords]
    
    return prefecture_dict

##################### 
# TILE ORGANIZATION #
#####################

def organize_by_prefecture(prefecture_city_dictionary, tile_dictionary):
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
    
    for prefecture, cities in prefecture_city_dict.items():
        for city in cities:
            try:
                prefecture_tile_dict[prefecture] += city_dict[city[0]]
            except:
                continue

    return prefecture_tile_dict

if __name__ == '__main__':

    # Read from JSON File
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)
    
    tile_dictionary = create_python_object(json_object)
    prefecture_city_dict = parse_scraped_info()
    prefecture_tile_dict = organize_by_prefecture(prefecture_city_dict, tile_dictionary)

    # Visualize data
    dv.plot_points_2d(tile_dictionary)
    dv.plot_points_2d(tile_dictionary, prefectures = prefecture_tile_dict)
    dv.plot_points_3d(tile_dictionary)
    dv.plot_points_3d(tile_dictionary, prefectures=prefecture_tile_dict)
    


        

