##### FILE FOR GENERATING ROUTING SCHEMES FOR PROBLEM INSTANCES #####

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


def gather_routing_info(mode_obj, serviced_aps_obj, contacted_sink_obj, tile_dict, tile_pdf_dict):
    """
    Given a mode obj, an ap object, and a sink object where the nodes of the ap and sink objects are all in contact with
    the nodes of the mode obj, gathers info to be used to generate a routing scheme
    """
    aps = set()
    sinks = set()
    ap_translate_dict = {}

    serviced_aps_obj.assign_ap_radius(tile_dict, tile_pdf_dict)
    to_delete = set()
    for ap, info in serviced_aps_obj.ap_dict.items():
        if info[1] == 0:
            to_delete.add(ap)
    for ap in to_delete:
        del serviced_aps_obj.ap_dict[ap]

    for ap, info in serviced_aps_obj.ap_dict.items():
        min_dist = 1000
        min_id = 'x'
        for node_id, node_info in mode_obj.mode_dict.items():
            node_coords = node_info['loc']
            dist = math.dist(node_coords, info[0])
            if dist < min_dist:
                min_dist = dist
                min_id = node_id
        ap_translate_dict[ap] = min_id
        aps.add(min_id)

    for sink, coords in contacted_sink_obj.sink_dict.items():
        min_dist = 1000
        min_id = 'x'
        for node_id, node_info in mode_obj.mode_dict.items():
            node_coords = node_info['loc']
            dist = math.dist(node_coords, coords)
            if dist < min_dist:
                min_dist = dist
                min_id = node_id

        sinks.add(min_id)

    aps = aps.difference(sinks)

    formatted_dict = {}
    translate_dict = {}
    counter = 1
    duplicated = set()

    # Add the AP's
    num_aps = 0

    for ap in aps:
    
        formatted_dict[counter] = mode_obj.mode_dict[ap]
        translate_dict[ap] = counter
        counter += 1
        num_aps += 1

        duplicated.add(ap)

    # Add the sinks
    num_sinks = 0 
    for sink in sinks:
        formatted_dict[counter] = mode_obj.mode_dict[sink]
        translate_dict[sink] = counter
        counter += 1
        num_sinks += 1

        duplicated.add(sink)
    

    # Add the rest
    num_others = 0
    for node, info in mode_obj.mode_dict.items():
        if node not in duplicated:
            formatted_dict[counter] =  mode_obj.mode_dict[node]
            translate_dict[node] = counter
            counter += 1
            num_others += 1
            duplicated.add(node)

    # Fix neighbors
    for node, info in formatted_dict.items():
        if len(info['neighbors']) == 1:
            formatted_dict[node]['neighbors'] =  [translate_dict[info['neighbors'][0]]]
        elif len(info['neighbors']) == 2:
            formatted_dict[node]['neighbors'] =  [translate_dict[info['neighbors'][0]], translate_dict[info['neighbors'][1]]]

    # Add edges
    edges = []
    for node, info in formatted_dict.items():
        neighbors = info['neighbors']
        for neighbor in neighbors:
            coords_1 = formatted_dict[node]['loc'][1], formatted_dict[node]['loc'][0]
            coords_2 = formatted_dict[neighbor]['loc'][1], formatted_dict[neighbor]['loc'][0]
            dist_in_km = haversine(coords_1, coords_2)
            time_dist = round(dist_in_km/mode_obj.speed * 60 + 10, 1)
            edges.append((node, neighbor, time_dist))
            edges.append((neighbor, node, time_dist))

    vehicle_capacity = mode_obj.capacity
    num_vehicles = mode_obj.num_vehicles

    people_rate_dict = {}
    for i in range(1, num_aps + 1):

        ap_key = 'x'
        ap_name = 'y'
        # Find entry in ap_object
        for key, val in translate_dict.items():
            if val == i:
                ap_key = key
        for name,val in ap_translate_dict.items():
            if val == ap_key:
                ap_name = name
        
        # Get number of people
        tiles_covered = ap_influence(tile_dict, serviced_aps_obj.ap_dict[ap_name][0],  serviced_aps_obj.ap_dict[ap_name][1])
        num_people = 0
        for tile in tiles_covered:
            num_people += tile_pdf_dict[tile]

        rate = num_people / (serviced_aps_obj.ap_dict[ap_name][1] * 100)

        people_rate_dict[i] = [num_people, rate]

    people_func = lambda x: people_rate_dict[x][0]
    rate_func = lambda x: people_rate_dict[x][1]
    percent_covered = serviced_aps_obj.get_percent_covered(tile_dict, tile_pdf_dict)

    return {
        'num_aps': num_aps,
        'num_sinks': num_sinks,
        'num_others': num_others,
        'edges': edges,
        'vehicle_capacity': vehicle_capacity,
        'num_vehicles': num_vehicles,
        'people_func': people_func,
        'rate_func': rate_func,
        'percent_covered': percent_covered
    }

def generate_routing_scheme(mode_obj, serviced_aps_obj, contacted_sink_obj, tile_dict, tile_pdf_dict, num_iterations):
    """
    Given a mode obj, an ap object, and a sink object where the nodes of the ap and sink objects are all in contact with
    the nodes of the mode obj, generates a routing scheme
    """
    routing_info = gather_routing_info(mode_obj, serviced_aps_obj, contacted_sink_obj, tile_dict, tile_pdf_dict)
    initial_graph = nx_graph(routing_info['num_aps'], routing_info['num_sinks'], routing_info['num_others'], routing_info['edges'])
    solver_instance = create_instance_of_solver(initial_graph)
    returned_object = vrptw_instance.create_complete_graph(solver_instance, routing_info['num_aps'], routing_info['num_sinks'], routing_info['num_others'])
    complete_graph_matrix, chosen_sink_matrix = returned_object[0], returned_object[1]
    complete_graph_object = nx_complete_graph(complete_graph_matrix)
    duplicated_complete_graph = vrptw_instance.assign_time_intervals(complete_graph_matrix, routing_info['people_func'], 
                                                                     routing_info['rate_func'], routing_info['vehicle_capacity'])
    duplicated_complete_graph_matrix = duplicated_complete_graph[0]
    time_windows = duplicated_complete_graph[1]
    problem_instance = vrptw_solver.create_model(duplicated_complete_graph_matrix, time_windows, routing_info['num_vehicles'],
                                                                                                routing_info['vehicle_capacity'],
                                                                                                )
    result = vrptw_solver.solve_model(problem_instance, num_iterations)
    solution = result.best
    routes = solution.get_routes()
    

    return routes, routing_info['percent_covered']

if __name__ == '__main__':

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']
    
    with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        sink_dict = data_dict['sink_dict']
    
    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        tile_dict = data_dict['tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']

    # Define objects
    ap_object = AssemblyPoint(ap_dict)
    sink_object = Sinks(sink_dict)
    mode = Mode(create_rail_object(), 300, 500, 10)
    contacted_aps = mode.get_contacted_aps(ap_object)
    contacted_sinks = mode.get_contacted_sinks(sink_object)

    # Give scheme
    routing_scheme = generate_routing_scheme(mode, contacted_aps, contacted_sinks, tile_dict, tile_pdf_dict, num_iterations=300)
    routes, percent_covered = routing_scheme[0], routing_scheme[1]
    time_of_neo = max([route.duration() for route in routes])
    
    print(time_of_neo, percent_covered)