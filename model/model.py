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
from routing_scheme import *


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

    tile_dict = dm.create_tile_dictionary(json_object)
    sink_object = Sinks(sink_dict)
    rail_object = Mode(create_rail_object(), speed = 300, capacity = 500, num_vehicles=20)
    road_object = Mode(create_road_object(), speed = 10, capacity = 50, num_vehicles = 100)

    rail_contacted_aps = rail_object.get_contacted_aps(ap_object)
    rail_contacted_sinks = rail_object.get_contacted_sinks(sink_object)

    remaining_aps = list(set(ap_object.ap_dict.keys()).difference(set(rail_contacted_aps.ap_dict.keys())))
    remaining_ap_dict = {k:v for (k,v) in zip(remaining_aps, [ap_object.ap_dict[ap] for ap in remaining_aps])}
    road_contacted_aps = AssemblyPoint(remaining_ap_dict)

    # Visualize data in 2D

    # Throws entire model onto a graph
    plot_points_2d(tile_dict, aps = ap_object, circles = True)
    plot_points_2d(tile_dict, aps = ap_object, sinks = sink_object, circles = True)
    plot_points_2d(tile_dict, aps = ap_object, bullet_train = rail_object, sinks = sink_object, circles = True)
    plot_points_2d(tile_dict, aps = ap_object, bullet_train = rail_object, road = road_object, sinks = sink_object, circles = True)

    # Partitions the AP's between modes and plots
    road_object.only_include_aps(road_contacted_aps)
    plot_points_2d(tile_dict, aps = rail_contacted_aps, sinks = rail_contacted_sinks, bullet_train = rail_object, circles = True)
    plot_points_2d(tile_dict, aps = road_contacted_aps, road = road_object, sinks = sink_object, circles = True)

    # Gives routing schemes
    rail_routing_scheme = generate_routing_scheme(rail_object, rail_contacted_aps, rail_contacted_sinks, tile_dict, tile_pdf_dict, num_iterations=300)
    road_routing_scheme = generate_routing_scheme(road_object, road_contacted_aps, sink_object, tile_dict, tile_pdf_dict, num_iterations=100, roads = True)
    road_routes, percent_covered = road_routing_scheme[0], road_routing_scheme[1]
    time_of_neo = max([route.duration() for route in road_routes])


