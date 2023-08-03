import geopandas as gpd
import matplotlib.pyplot as plt
import math
from matplotlib import collections  as mc
import json
from geopy import distance
import pandas as pd
import pickle
import os
import sys


# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

def create_rail_object():
    """
    Reads from JSON file to create python object of bullet train network
    """

    # Forcing path to be parent directory
    os.chdir(parent_dir)

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

    # Forcing path to be parent directory
    os.chdir(parent_dir)

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']

    with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        sink_dict = data_dict['sink_dict']

    df = pd.read_csv('./transportation/data/Bus_routes.csv')
    holder_graph = {}
    counter = 0
    ap_set = set()
    sink_set = set()
    for row in df['Assembly Point']:
        ap_set.add(row)
    for row in df['Sink']:
        sink_set.add(row)
    
    for ap in ap_set:
        holder_graph[ap] = counter
        counter += 1
    for sink in sink_set:
        holder_graph[sink] = counter
        counter += 1
    
    neighbor_dict = {}
    for ix in holder_graph.values():
        neighbor_dict[ix] = set()
    for ix, row in df.iterrows():
        index = holder_graph[row['Assembly Point']]
        sink_index = (holder_graph[row['Sink']])
        travel_time = round(row['Total_TravelTime'])
        neighbor_elt = (sink_index, travel_time)
        neighbor_dict[index].add(neighbor_elt)

    # Construct road graph
    road_graph = {k:v for (v,k) in holder_graph.items()}

    # Fix inconsistencies
    for k,v in road_graph.items():
        if v == 'Chichibunomiya Rugby':
            road_graph[k] = 'Chichibunomiya Rugby '
        if v == 'US Embassy':
            road_graph[k] = 'US Embassy '

    # Add initial neighbors
    for key, neighbors in neighbor_dict.items():
        if road_graph[key] in ap_dict:
            road_graph[key] = {'loc': ap_dict[road_graph[key]][0], 'neighbors': neighbors}
        else:
            road_graph[key] = {'loc': sink_dict[road_graph[key]], 'neighbors': neighbors}
        
    # Transfer location data to sinks
    for k,v in road_graph.items():
        if type(v) == str:
            road_graph[k] = {'loc': sink_dict[v], 'neighbors': set()}
    
    # Fix sink neighbors
    for k,v in road_graph.items():
        for neighbor in v['neighbors']:
            road_graph[neighbor[0]]['neighbors'].add((k, neighbor[1]))
    return road_graph


if __name__ == '__main__':
    train_graph = create_rail_object()
    road_graph = create_road_object()
    




