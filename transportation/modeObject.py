
import os
import sys
import pickle

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import math
from transportation.constructingModes import *
from assemblyPoints.apObject import *
from sinks.sinkObject import *

class Mode:

    def __init__(self, mode_dictionary, speed, capacity, num_vehicles):
        """
        Given a dictionary that contains node_id's as keys and a values as tuples with 2 elements,
        the first being coordinates and the second being a neighbor set containing other node_ids,
        constructs a Mode object
        """
        # Want to retain dictionary for bookkeeping purposes
        self.mode_dict = mode_dictionary
        self.speed = speed
        self.capacity = capacity
        self.num_vehicles = num_vehicles

    def get_coords(self):
        """
        Returns a list of the coordinates of the network nodes in no particular order
        """
        coords_list = []
        for node_id, node_info in self.mode_dict.items():
            coords_list.append(node_info['loc'])
        
        return coords_list
    
    def get_contacted_aps(self, ap_object):
        """
        Given an AP dictionary of the form {"Name_of_ap": (coordinates, radius)}, returns another dictionary
        that contains the ap's that are able to be serviced by the mode 
        """
        contacted_aps = {}
        coords_list = self.get_coords()

        for ap, info in ap_object.ap_dict.items():
            coords = info[0]

            for network_coords in coords_list:
                if math.dist(coords, network_coords) < .15:
                    contacted_aps[ap] = (coords, info[1])

        return AssemblyPoint(contacted_aps)

    def get_contacted_sinks(self, sink_object):

        """
        Given a sink object, returns another dictionary
        that contains the ap's that are able to be serviced by the mode 
        """
        contacted_sinks = {}
        coords_list = self.get_coords()

        for sink, coords in sink_object.sink_dict.items():
            for network_coords in coords_list:
                if math.dist(coords, network_coords) < .1:
                    contacted_sinks[sink] = coords

        return Sinks(contacted_sinks)

    def only_include_aps(self, ap_object):
        """
        ONLY FOR ROAD OBJECT.
        Given an ap object, modifies the mode dictionary to only include vertices that have those points on them
        """
        to_keep = set()
        new_mode_dict = {}
        for key, val in self.mode_dict.items():
            go_on = True
            for ap in ap_object.ap_dict.values():
                if math.dist(val['loc'], ap[0]) < .01:
                    to_keep.add(key)
                    break
        
        for index in to_keep:
            new_mode_dict[index] = self.mode_dict[index]
        
        # Include sinks
        neighbor_dict = {}
        for k,v in new_mode_dict.items():
            for neighbor in v['neighbors']:
                neighbor_ix = neighbor[0]
                included = set()
                for neighbors in self.mode_dict[neighbor_ix]['neighbors']:
                    if neighbor[0] in new_mode_dict:
                        included.add(neighbor)
                neighbor_dict[neighbor_ix] =  {'loc':self.mode_dict[neighbor_ix]['loc'], 'neighbors': included}

        for ix, info in neighbor_dict.items():
             new_mode_dict[ix] = {'loc':self.mode_dict[ix]['loc'], 'neighbors': included}

        self.mode_dict = new_mode_dict 

if __name__ == "__main__":

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']

    with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        sink_dict = data_dict['sink_dict']

    bullet_train_graph = create_rail_object()
    ap_obj = AssemblyPoint(ap_dict)
    sink_obj = Sinks(sink_dict)
    mode = Mode(bullet_train_graph, 200, 500, 20)
    contacted_aps = mode.get_contacted_aps(ap_obj)
    contacted_sinks = mode.get_contacted_sinks(sink_obj)


    
    
    




