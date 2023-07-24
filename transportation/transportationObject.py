import geopandas as gpd
import matplotlib.pyplot as plt
import math
from matplotlib import collections  as mc
import json
from geopy import distance

def create_rail_objects():
    """
    Reads from JSON file to create python object of bullet train network
    """
    # Read and extract info from files
    with open('./transportation/data/json_files/bullet_train.json') as f:
        json_obj = json.load(f)

    rail_stations = gpd.read_file('./transportation/data/rstatp_jpn.shp', encoding = 'latin1')
    station_obj = rail_stations['geometry']
    stations = list(zip(station_obj.x, station_obj.y))

    edges = []
    for feature in json_obj['features']:
        edges.append(feature['geometry']['coordinates'])

    rail_stations = gpd.read_file('./transportation/data/rstatp_jpn.shp', encoding = 'latin1')
    station_obj = rail_stations['geometry']
    stations = list(zip(station_obj.x, station_obj.y))
    
    # Build bullet train representation


if __name__ == '__main__':
    create_rail_objects()




