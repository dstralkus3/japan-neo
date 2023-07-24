
import sys
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data_manipulation as dm
import pickle
import json
from relevant_data.scraping import *
import geopandas

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from assemblyPoints.ap import *
from transportation.transportationObject import *

###########################
# SUPPORT FOR 2D PLOTTING #
###########################

def plot_points_2d(tile_dictionary, point_size=2, prefectures = None, aps = None, covered = set(), 
                   circles = None, rail = False):
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
                colors.append('slategrey')
            
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    circle_data = []

    # If aps are given, highlight them. If they are given radius, add a datapoint to circle_data to draw the circle
    if aps:
        for info in aps.values():
            coords = info[0]
            radius = info[1]
            if radius > 0:
                circle_data.append((coords, radius))
            x_values.append(coords[1])
            y_values.append(coords[0])
            colors.append('red')
            sizes.append(5)

    ax.scatter(x_values, y_values, c = colors, s = sizes)

    # Draw circles if any
    if circle_data:
        for circle in circle_data:
            coords = (circle[0][1], circle[0][0])
            radius = circle[1]
            circle = plt.Circle(coords, radius, color='red', fill=False)
            plt.gca().add_artist(circle)

    if rail == True:
        rail_stations = gpd.read_file('./transportation/data/rstatp_jpn.shp', encoding='latin1')
        rail_line = gpd.read_file('./transportation/data/raill_jpn.shp', encoding='latin1')
        rail_line.plot(ax=ax, color='yellow', linewidth=.4, label='Rail Lines')
        rail_stations.plot(ax=ax, color='black', markersize=5, label='Rail Stations')

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.grid(True)
    plt.xlim(120, 155)
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

    # Choose ap_dict at random

    tile_dict = dm.create_tile_dictionary(json_object)
    # radii_assignment = assign_ap_radius(ap_dict, tile_dict, tile_pdf_dict)
    # updated_ap_dict, percent_covered = radii_assignment[0], radii_assignment[1]
    # tiles_covered = get_tiles_covered(tile_dict, updated_ap_dict)

    # Visualize data in 2D
    plot_points_2d(tile_dict, aps = ap_dict, rail = True)

    # Visualize data in 3D
    # plot_points_3d(tile_dictionary)
    # plot_points_3d(tile_dictionary, prefectures=prefecture_tile_dict)
    # plot_points_3d(tile_dictionary, prefectures=prefecture_tile_dict, tile_pdf = normalized_pdf_dict)
    