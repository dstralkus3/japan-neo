
import sys
import os

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Imports from packages in PIP
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle
import json
import geopandas
from matplotlib.collections import LineCollection

# Imports from within directory
from assemblyPoints.apObject import *
from transportation.constructingModes import *
from transportation.modeObject import *
from population.relevant_data.scraping import *
import population.data_manipulation as dm
from sinks.sinkObject import *

###########################
# SUPPORT FOR 2D PLOTTING #
###########################

def plot_points_2d(tile_dictionary, point_size=1, prefectures = None, aps = None, covered = set(), 
                    bullet_train = None, sinks = None, circles = False):
    """
    Given a tile dictionary, plots a list of 2D points in R^2 using matplotlib. Distinguishes between prefectures if 
    prefecture dictionary of the form returned by organize by prefecture is passed in.
    """
    fig, ax = plt.subplots()
    color_list = ['red', 'blue', 'black', 'yellow', 'orange', 'pink', 'purple']
    sizes = [point_size for x in range(len(tile_dictionary.keys()))]

    # If prefectures are given, color tiles in accordance with the prefectures
    if prefectures:
        tile_set = set()
        points = []
        colors = []
        counter = 0 
        for prefecture, tiles in prefectures.items():
            color = color_list[counter]
            for tile in tiles:
                if tile not in tile_set:
                    points.append(tile_dictionary[tile])
                    if tile not in covered:
                        colors.append(color)
                    else:
                        colors.append('red')
                    tile_set.add(tile)
                else:
                    continue
            counter += 1
            counter %= 7
    else:
        points = []
        colors = []
        for i, coords in tile_dictionary.items():
            points.append(coords)
            if i in covered:
                colors.append('red')
            else:
                colors.append('silver')
            
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    circle_data = []

    # If aps are given, highlight them. If they are given radius, add a datapoint to circle_data to draw the circle
    if aps:
        ap_dict = aps.ap_dict
        for info in ap_dict.values():
            coords = info[0]
            radius = info[1]
            if radius > 0:
                circle_data.append((coords, radius))
            x_values.append(coords[0])
            y_values.append(coords[1])
            colors.append('red')
            sizes.append(3)

    # Draw circles if any. This is specified by the radii in the ap_dict

    if circle_data and circles == True:
        for circle in circle_data:
            coords = (circle[0][0], circle[0][1])
            radius = circle[1]
            circle = plt.Circle(coords, radius, color='red', fill=False)
            plt.gca().add_artist(circle)

    if sinks:
        sink_dict = sinks.sink_dict
        for coords in sink_dict.values():
            x_values.append(coords[0])
            y_values.append(coords[1])
            colors.append('blue')
            sizes.append(3)

    if bullet_train:

        mode_dictionary = bullet_train.mode_dict
        segments = set()

        for id, info in mode_dictionary.items():

            # Add node to graph
            x_values.append(info['loc'][0])
            y_values.append(info['loc'][1])
            colors.append('black')
            sizes.append(.3)
        
            # Add line segments
            for neighbor in info['neighbors']:
                new_segment = (info['loc'], mode_dictionary[neighbor]['loc'])
                if new_segment not in segments and (new_segment[1], new_segment[0]) not in segments:
                    segments.add(new_segment)
        
        lc = LineCollection(segments)
        lc.set_color('black')
        ax.add_collection(lc)

    ax.scatter(x_values, y_values, c = colors, s = sizes)
    width_ratio = .9  # Increase this value to elongate more
    height_ratio = 1  # Keep this value as 1 for no change in height
    ax.set_aspect(aspect=width_ratio / height_ratio)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.grid(True)
    plt.xlim(127, 146.5)
    plt.ylim(27, 46)

    plt.show()

###########################
# SUPPORT FOR 3D PLOTTING #
###########################

def plot_points_3d(tile_dictionary, point_size = 2, prefectures = None, tile_pdf = None):
    """
    Plots a list of 2D points in R^3 using matplotlib.
    """
    color_list = ['red', 'blue', 'black', 'yellow', 'orange', 'pink', 'purple']
    counter = 0 
    points = []
    colors = []

    if tile_pdf:
        new_tile_dictionary = {}
        for ix, coords in tile_dictionary.items():
            new_tile_dictionary[ix] = [coords[0], coords[1], tile_pdf[ix]]
        tile_dictionary = new_tile_dictionary
    
    if prefectures:
        for prefecture, tiles in prefectures.items():
            color = color_list[counter]
            for tile in tiles:
                points.append(tile_dictionary[tile])
                colors.append(color)
            counter += 1
            counter %= 7
    else:
        points = tile_dictionary.values()
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    if tile_pdf:
        z_values = [point[2] for point in points]  # Set z-coordinates to 0 for the 3D plane
    else:
        z_values = [0 for point in points] 

    if prefectures:
        if tile_pdf:
            ax.scatter(x_values, y_values, z_values, c = colors, s = point_size)
            ax.set_title('Japan Geometry with Prefectures with Population')

        else:
            ax.scatter(x_values, y_values, z_values, c = colors, s = point_size)
            ax.set_title('Japan Geometry with Prefectures without Population')
    else:
        ax.scatter(x_values, y_values, z_values, s = point_size)
        if tile_pdf:
            ax.set_title('Japan Geometry without Prefectures with Population')
        else:
            ax.set_title('Japan Geometry without Prefectures without Population')
        
    ax.set_xlabel('Latitude')
    ax.set_ylabel('Longitude')

    # Adjust the viewing limits (zoom in)
    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))


    plt.tight_layout()  
    plt.show()

if __name__ == '__main__':

    # Load relevant data
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)
    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as file:
        data_dict = pickle.load(file)
        prefecture_tile_dict = data_dict['prefecture_tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']
        normalized_pdf_dict = data_dict['normalized_tile_pdf_dict']

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']
    
    with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        sink_dict = data_dict['sink_dict']

    tile_dict = dm.create_tile_dictionary(json_object)
    ap_object = AssemblyPoint(ap_dict)
    test_ap_object = AssemblyPoint({'Fukui Prefectural Stadium': ([136.18272, 36.05188], 0), 'Obihiro Athletics Stadium': ([143.14523, 42.89413], 0), 'Nagoya Dome': ([136.94739, 35.186], 0), 'Sasebo Navy Base': ([129.71534, 33.16715], 0), 'Komazawa Olympic Stadium': ([139.66364, 35.62557], 0)})
    test_ap_object.assign_ap_radius(tile_dict, tile_pdf_dict)

    sink_object = Sinks(sink_dict)
    bullet_train_mode = Mode(create_rail_object(), speed = 300, capacity = 500, num_vehicles=20)
    contacted_aps = bullet_train_mode.get_contacted_aps(ap_object)
    contacted_aps.assign_ap_radius(tile_dict, tile_pdf_dict)
    contacted_sinks = bullet_train_mode.get_contacted_sinks(sink_object)

    # Visualize data in 2D
    plot_points_2d(tile_dict, aps = ap_object, bullet_train = bullet_train_mode, sinks = contacted_sinks, circles = True)
    
    