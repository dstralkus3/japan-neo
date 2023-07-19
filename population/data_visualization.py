
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import data_manipulation as dm

###############################
# FUNCTIONS TO VISUALIZE DATA #
###############################

def plot_points_2d(points, point_size=2, prefectures = None):
    """
    Plots a list of 2D points in R^2 using matplotlib. Distinguishes between prefectures if 
    prefecture dictionary of the form returned by organize by prefecture is passed in.
    """
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.scatter(x_values, y_values, s=point_size)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Discretized Geometry')
    plt.grid(True)
    plt.show()

def plot_points_3d(points, point_size = 2):
    """
    Plots a list of 2D points in R^3 using matplotlib.
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    z_values = [0] * len(points)  # Set z-coordinates to 0 for the 3D plane

    ax.scatter(x_values, y_values, z_values, s = point_size)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Discretized Geometry')

     # Adjust the viewing limits (zoom in)
    ax.set_xlim(min(x_values), max(x_values))
    ax.set_ylim(min(y_values), max(y_values))
    ax.set_zlim(-.1,.1)  # Set z-limits based on your requirements

    plt.tight_layout()  
    plt.show()


if __name__ == '__main__':
    pass