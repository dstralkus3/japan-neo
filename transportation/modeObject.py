
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

class Mode:

    def __init__(self, mode_dictionary, speed):
        """
        Given a dictionary that contains node_id's as keys and a values as tuples with 2 elements,
        the first being coordinates and the second being a neighbor set containing other node_ids,
        constructs a Mode object
        """
        # Want to retain dictionary for book keeping purposes
        self.mode_dict = mode_dictionary
        self.speed = speed
    
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
                if math.dist(coords, network_coords) < .2:
                    contacted_aps[ap] = (coords, info[1])

        return AssemblyPoint(contacted_aps)
    


if __name__ == "__main__":

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']

    bullet_train_graph = create_rail_object()
    ap_obj = AssemblyPoint(ap_dict)
    mode = Mode(bullet_train_graph, 200)
    contacted_aps = mode.get_contacted_aps(ap_obj)
    

    
    
    




