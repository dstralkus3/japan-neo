
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data_manipulation as dm
import pickle
import json
from relevant_data.scraping import *

###########################
# SUPPORT FOR 2D PLOTTING #
###########################

def plot_points_2d(tile_dictionary, point_size=2, prefectures = None):
    """
    Given a tile dictionary, plots a list of 2D points in R^2 using matplotlib. Distinguishes between prefectures if 
    prefecture dictionary of the form returned by organize by prefecture is passed in.
    """
    color_list = ['red', 'blue', 'black', 'yellow', 'orange', 'pink', 'purple']
    counter = 0 
    points = []
    colors = []

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

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    if colors:
        plt.scatter(x_values, y_values, c = colors, s = point_size)
        plt.title('Japan Geometry with Prefectures')
    else:
        plt.scatter(x_values, y_values, s = point_size)
        plt.title('Japan Geometry without Prefectures')

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.grid(True)
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

            # Uncomment to draw lines from (x,y) to (z)
            # for i in range(len(x_values)):
            #     # Draw the line from (x, y) to (x, y, z)
            #     ax.plot([x_values[i], x_values[i]], [y_values[i], y_values[i]], [0, z_values[i]], color=colors[i], linestyle='-')

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
    ax.set_zlim(-.25,.25)  # Set z-limits based on your requirements

    plt.tight_layout()  
    plt.show()


if __name__ == '__main__':

    # Load relevant data
    with open('geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)
    with open('./population/relevant_data/pickleFiles/pickledData.pkl', 'rb') as file:
        data_dict = pickle.load(file)
        prefecture_tile_dict = data_dict['prefecture_tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']

    tile_dictionary = dm.create_tile_dictionary(json_object)

    # Visualize data
    plot_points_3d(tile_dictionary)
    plot_points_3d(tile_dictionary, prefectures=prefecture_tile_dict)
    plot_points_3d(tile_dictionary, prefectures=prefecture_tile_dict, tile_pdf = tile_pdf_dict)