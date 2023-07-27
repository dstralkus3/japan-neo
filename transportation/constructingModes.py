import geopandas as gpd
import matplotlib.pyplot as plt
import math
from matplotlib import collections  as mc
import json
from geopy import distance
import csv

def create_rail_object():
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
    bullet_train_graph = {}
    counter = 0
    for station in stations:
        bullet_train_graph[counter] = {'loc': station}
        counter += 1

    # Modify edges to be in terms of node ID's
    edge_ids = []
    for edge in edges:
        new_edge = ['x', 'y']
        # Find corresponding entries
        for k,v in bullet_train_graph.items():
            if math.dist(v['loc'], edge[0]) < .027:
                new_edge[0] = k
            elif math.dist(v['loc'], edge[1]) < .027:
                new_edge[1] = k
            else:
                continue
        edge_ids.append(new_edge)

    # Populate neighbors of each node
    for edge in edge_ids:

        # Support for pre node
        if 'neighbors' not in bullet_train_graph[edge[0]]:
            bullet_train_graph[edge[0]]['neighbors'] = [edge[1]]
        else:
            bullet_train_graph[edge[0]]['neighbors'].append(edge[1])
        
         # Support for post node
        if 'neighbors' not in bullet_train_graph[edge[1]]:
            bullet_train_graph[edge[1]]['neighbors'] = [edge[0]]
        else:
            bullet_train_graph[edge[1]]['neighbors'].append(edge[0])
    
    to_delete = []
    for id, info in bullet_train_graph.items():
        if 'neighbors' not in info:
            to_delete.append(id)
    for id in to_delete:
        del bullet_train_graph[id]

    return bullet_train_graph




def create_road_object():


    return




    
if __name__ == '__main__':
    bullet_train_graph = create_rail_object()
    




