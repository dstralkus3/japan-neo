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
    # Append system path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.append(parent_dir)
    #print("The Current working directory is: {0}".format(os.getcwd()))
    # Forcing path to be parent directory
    os.chdir(parent_dir)
    #print("The Current working directory is: {0}".format(os.getcwd()))

    # Load relevant data
    with open('./geometry/geometries/finer_grain.json') as file:
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
    x_vals = []
    y_vals = []
    dist_list = [.05, .06,.07,.08,.09,.10,.11,.12,.13,.14,.15,.16,.17,.18,.19,.20]
    for i in range(0,16):
        print("Im here")
        rail_object = Mode(create_rail_object(), speed = 300, capacity = 500, num_vehicles=20)
        rail_contacted_aps = rail_object.get_contacted_aps(ap_object, dist = dist_list[i])
        rail_contacted_sinks = rail_object.get_contacted_sinks(sink_object)
        remaining_aps = list(set(ap_object.ap_dict.keys()).difference(set(rail_contacted_aps.ap_dict.keys())))
        remaining_ap_dict = {k:v for (k,v) in zip(remaining_aps, [ap_object.ap_dict[ap] for ap in remaining_aps])}
        road_contacted_aps = AssemblyPoint(remaining_ap_dict)
        road_object = Mode(create_road_object(), speed = 10, capacity = 50, num_vehicles = 50)
        road_object.only_include_aps(road_contacted_aps)
        rail_routing_scheme = generate_routing_scheme(rail_object, rail_contacted_aps, sink_object, tile_dict, tile_pdf_dict, num_iterations=200, roads = False)
        rail_routes, rail_percent_covered = rail_routing_scheme[0], rail_routing_scheme[1]
        road_routing_scheme = generate_routing_scheme(road_object, road_contacted_aps, sink_object, tile_dict, tile_pdf_dict, num_iterations=200, roads = True)
        road_routes, road_percent_covered = road_routing_scheme[0], road_routing_scheme[1]
        time_of_road_routing = max([route.duration() for route in road_routes])
        time_of_rail_routing = max(route.duration() for route in rail_routes)
        time_of_neo = max(time_of_rail_routing, time_of_road_routing)
        x_vals.append(dist_list[i])
        y_vals.append(time_of_neo)

    print(x_vals, y_vals)

    # plt.scatter(x_vals, y_vals)
    # plt.xlabel('Number of Buses')
    # plt.ylabel('Time of NEO')
    # plt.title('Effect of Number of Buses on Time of NEO')
    # plt.show()



     # Visualize data in 2D

    # Throws entire model onto a graph
    # plot_points_2d(tile_dict, aps = ap_object, circles = True)
    # plot_points_2d(tile_dict, aps = ap_object, sinks = sink_object, circles = True)
    # plot_points_2d(tile_dict, aps = ap_object, bullet_train = rail_object, sinks = sink_object, circles = True)
    # plot_points_2d(tile_dict, aps = ap_object, bullet_train = rail_object, road = road_object, sinks = sink_object, circles = True)

    # # Partitions the AP's between modes and plots
    
    # plot_points_2d(tile_dict, aps = rail_contacted_aps, sinks = rail_contacted_sinks, bullet_train = rail_object, circles = True)
    # plot_points_2d(tile_dict, aps = road_contacted_aps, road = road_object, sinks = sink_object, circles = True)

    # Gives routing schemes