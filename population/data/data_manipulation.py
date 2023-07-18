
import json
import numpy as np
import data_visualization as dv

#####################
# DATA MANIPULATION #
#####################

def create_python_object(json_object):
    """
    Given a json object of the form found in geometry/geometries, returns a python dictionary of the tile centers.
    """
    tiles = json_object['features']
    tile_dictionary = {}
    counter = 0
    for tile in tiles:

        # Find center of each tile
        coordinates = tile['geometry']['coordinates'][0]
        bottom_left, top_left, top_right = coordinates[0], coordinates[1], coordinates[2]
        mid_left = (bottom_left[0], (bottom_left[1] + top_left[1])/2)
        mid_top = ((top_left[0] + top_right[0])/2, top_left[1])
        center = (mid_top[0], mid_left[1])

        # Populate dictionary
        tile_dictionary[counter] = center
        counter += 1        

    return tile_dictionary


if __name__ == '__main__':

    # Read from JSON File
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)

    # Create python object
    tile_dictionary = create_python_object(json_object)

    # Visualize data
    dv.plot_points_2d(tile_dictionary.values())


        

