##### FILE FOR GENERATING MODEl #####

import os
import sys

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Imports from PIP
from haversine import haversine, Unit
import pickle

# Imports from directory
from assemblyPoints.apObject import *
from sinks.sinkObject import *
from transportation.constructingModes import *
from transportation.modeObject import *
from routing.solver.vrptw_instance import *
from routing.solver.vrptw_solver import *
from routing.visualization.graph_visualization import *
from visualization.data_visualization import *


if __name__ == '__main__':

    # Load relevant data
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)
        tile_dict = dm.create_tile_dictionary(json_object)

    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as file:
        data_dict = pickle.load(file)
        prefecture_tile_dict = data_dict['prefecture_tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']
        normalized_pdf_dict = data_dict['normalized_tile_pdf_dict']

    with open('./model/pickleFiles/model_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_object = data_dict['apChoice']
    
    with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        sink_dict = data_dict['sink_dict']
    
    ####################################################################################

    train_object = Mode(create_rail_object(), 200, 500, 10)
    train_ap_object = train_object.get_contacted_aps(ap_object)
    
    #road_object = Mode()
    road_aps = set(ap_object.ap_dict.keys()).difference(set(train_ap_object.ap_dict.keys()))
    road_ap_object = AssemblyPoint({k:v for (k,v) in zip(road_aps, [ap_object.ap_dict[ap] for ap in road_aps])})
    
    plot_points_2d(tile_dict, aps = train_ap_object, circles = True, bullet_train= train_object)
    plot_points_2d(tile_dict, aps = road_ap_object, circles = True, bullet_train= train_object)