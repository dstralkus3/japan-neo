
import json
import numpy as np
import data_visualization as dv
import reverse_geocode
import requests
from bs4 import BeautifulSoup

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

def get_city(latitude, longitude):
    location = reverse_geocode.get((longitude, latitude))
    if location['country_code'] == 'JP':
        return location['city']
    else:
        return 'Not in Japan'

def gather_cities_from_prefectures():
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
                        if title:
                            parsed.append(title)
                if parsed != None:
                    container_list.append(parsed)
            break
    
    # Parse city list further to create dictionary
    prefecture_dictionary = {}
    del container_list[0]
    for city_prefecture_pair in container_list:
        city_info = city_prefecture_pair[0] 
        prefecture_info = city_prefecture_pair[1] 
        if ',' in city_info:
            city = city_info.split(",")[0].strip()
        else:
            city = city_info
        prefecture = prefecture_info.split()[0]
        
        # Add to dictionary if not there already
        if prefecture in prefecture_dictionary:
            prefecture_dictionary[prefecture].append(city)
        else:
            prefecture_dictionary[prefecture] = [city]

    return prefecture_dictionary

#####################
# TILE ORGANIZATION #
#####################

def organize_by_city(tile_dictionary):
    """
    Given a tile dictionary of the formed returned by create_python_object(), returns a dictionary with key-value pairs
    as prefectures with the corresponding keys of the tile dictionary that are located in that prefecture
    """
    city_dictionary = {}
    for ix, tile in tile_dictionary.items():
        city = get_city(tile[0], tile[1])

        # Add to prefecture dictionary if not present
        if city not in city_dictionary:
            city_dictionary[city] = [ix]
        else:
            city_dictionary[city].append(ix)

    return city_dictionary

def organize_by_prefecture(city_prefecture_dictionary, city_dictionary):
    """
    Given city_prefecture_dict returned by  gather_cities_from_prefectures() and a city dictionary of 
    the form returned by organize_by_city(), creates a dictionary with prefectures as keys and tiles as values.
    """
    prefecture_dictionary = {}
    for prefecture, cities in city_prefecture_dictionary.items():
        node_list = []
        for city in cities:
            if city in city_dictionary:
                node_list += city_dictionary[city]
        prefecture_dictionary[prefecture] = node_list

    return prefecture_dictionary

if __name__ == '__main__':

    # Read from JSON File
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)

    # Create python object
    tile_dictionary = create_python_object(json_object)
    
    



"""
For each 

Motomachi
"""



        

