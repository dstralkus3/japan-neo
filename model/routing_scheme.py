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
from assemblyPoints.apObject import *
from sinks.sinkObject import *
from transportation.constructingModes import *
from transportation.modeObject import *

def gather_routing_info(mode_obj, serviced_aps_obj, contacted_sink_obj, tile_dict, tile_pdf_dict):
    """
    Given a mode obj, an ap object, and a sink object where the nodes of the ap and sink objects are all in contact with
    the nodes of the mode obj, gathers info to be used to generate a routing scheme
    """
    aps = set()
    sinks = set()
    ap_translate_dict = {}

    serviced_aps_obj.assign_ap_radius(tile_dict, tile_pdf_dict)

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
    
    vehicle_capacity = mode_obj.capacity
    num_vehicles = mode_obj.num_vehicles

    print(serviced_aps_obj.ap_dict)
    print(ap_translate_dict)
    print(translate_dict)


def generate_routing_scheme(mode_obj, serviced_aps_obj, contacted_sink_obj):
    """
    Given a mode obj, an ap object, and a sink object where the nodes of the ap and sink objects are all in contact with
    the nodes of the mode obj, generates a routing scheme
    """
    pass

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

    ap_object = AssemblyPoint(ap_dict)
    sink_object = Sinks(sink_dict)
    mode = Mode(create_rail_object(), 300, 500, 20)
    contacted_aps = mode.get_contacted_aps(ap_object)
    contacted_sinks = mode.get_contacted_sinks(sink_object)
    routing_info = gather_routing_info(mode, contacted_aps, contacted_sinks, tile_dict, tile_pdf_dict)
