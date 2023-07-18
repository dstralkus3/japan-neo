################################
# PATH REDIRECTION AND IMPORTS #
################################

import sys
import os

# Redirect path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from pyvis.network import Network
import networkx as nx
import numpy as np
import time
import random
import copy
from solver import vrptw_instance
from solver import vrptw_solver

###################################
# SUPPORT FOR GRAPH VISUALIZATION #
###################################

def nx_graph(num_aps, num_sinks, num_other, edges):
    """
    Creates a graph instance with a specified number of AP's, sinks, and other nodes. The input edges is a list of 3-tuples, where
    a 3-tuple (u,v,w) represents a di-edge from node u to node v with weight w. Note, nodes are 1-indexed (no 0th node).
    """

    # Create a graph instance
    nx_graph = nx.DiGraph()

    # Create AP's
    for i in range(num_aps):
        nx_graph.add_node(i + 1, shape = 'image', image = 'icons/ap.png')

    # Create sinks
    for j in range(num_aps, num_aps + num_sinks):
        nx_graph.add_node(j + 1, shape = 'image', image = 'icons/sink.png')

    # Create other nodes
    for k in range(num_sinks + num_aps, num_sinks + num_aps + num_other):
        nx_graph.add_node(k + 1, shape = 'image', image = 'icons/node.png')

    for edge in edges:
        nx_graph.add_edge(edge[0], edge[1], title = edge[2])
    
    return nx_graph

def visualize_graph(G):
    """
    Given a graph of the form returned by create_graph(), visualizes network.
     
    Writes to a file in visualization folder. To display, manually load HTML file into a browser. 
    On VSCode, download the extension 'Open with Browser', then go to your directory, right click the
    html file, and open with chrome. An interactive network will open.
    """
    net = Network(notebook=True, cdn_resources='remote')
    net.from_nx(G)
    net.show('visualization/full_graph_visual.html')

def nx_complete_graph(G):
    """
    Given an adjacency matrix of the form returned by create_complete_graph in vrptw.py,
    creates a nx graph object, ready to be visualized.
    """
    # Create a graph instance
    nx_complete_graph = nx.complete_graph(len(G), nx.DiGraph())

    # Set icons
    nx.set_node_attributes(nx_complete_graph, {0: 'image'}, 'shape')
    nx.set_node_attributes(nx_complete_graph, {0: 'icons/depot.png'}, 'image')

    for i in range(1, len(G)):
        nx.set_node_attributes(nx_complete_graph, {i: 'image'}, 'shape')
        nx.set_node_attributes(nx_complete_graph, {i: 'icons/ap.png'}, 'image')

    # Set edge weights
    for i in range(len(G)):
        for j in range(len(G)):
            nx.set_edge_attributes(nx_complete_graph, {(i,j): G[i][j]}, 'title')
    
    return nx_complete_graph


def visualize_complete_graph(G):
    """
    Given a graph object of the form returned by nx_complete_graph, write an html file in visualization
    to visualize graph.
    """
    net = Network(notebook=True, cdn_resources='remote')
    net.from_nx(G)
    net.show('visualization/complete_graph_visual.html')

def nx_duplicated_complete_graph(G, time_windows, duplication_stats):
    """
    Given an adjacency matrix of the form returned by assign_time_intervals in vrptw.py,
    creates a nx graph object, ready to be visualized.
    """
    nx_duplicated_complete_graph = nx.complete_graph(len(G), nx.DiGraph(), )

    # Set icons
    nx.set_node_attributes(nx_duplicated_complete_graph, {0: 'image'}, 'shape')
    nx.set_node_attributes(nx_duplicated_complete_graph, {0: 'icons/depot.png'}, 'image')

    # Set node attributes
    counter = 1
    for i, stats in duplication_stats.items():
        if i % 7 == 0:
            color = 7
        else:
          color = i % 7
        num_duplications = stats[0]
        for j in range(num_duplications):
            nx.set_node_attributes(nx_duplicated_complete_graph, {counter:'image'}, 'shape')
            nx.set_node_attributes(nx_duplicated_complete_graph, {counter:f'icons/duplicatedAps/ap{color}.png'}, 'image')
            counter += 1

    for i in range(len(G)):
        nx.set_node_attributes(nx_duplicated_complete_graph, {i:time_windows[i]}, 'label')

    # Set edge attributes
    return nx_duplicated_complete_graph
 
def visualize_duplicated_complete_graph(G):
    """
    Given a graph object of the form returned by visualize_duplicated_complete_graph(),
    writes an html file in visualization folder.
    """
    net = Network(notebook=True, cdn_resources = 'remote')
    net.force_atlas_2based()
    net.from_nx(G)
    net.show('visualization/duplicated_complete_graph_visual.html')

def add_routes(duplicated_complete_graph, routes):
    """
    Given a duplicated complete graph returned from nx_duplicated_complete_graph, and routes
    returned from the vrptw solver, highlights those routes in the complete graph.
    """
    used_edges = []
    counter = 0
    colors = ['red', 'orange', 'pink', 'purple', 'green', 'blue', 'black', 'teal']
    for route in routes:
        color = colors[counter]
        relevant_edges = [(0,route[0])]
        for i in range(len(route) - 1):
            relevant_edges.append((route[i], route[i + 1]))
        relevant_edges.append((route[-1], 0))
        used_edges += relevant_edges
        for edge in relevant_edges:
            nx.set_edge_attributes(duplicated_complete_graph, {edge: 5}, 'weight')
            nx.set_edge_attributes(duplicated_complete_graph, {edge: color}, 'color')
        counter = (counter + 1) % len(colors)

    # Removes un-utilized edges
    for edge in  copy.deepcopy(duplicated_complete_graph.edges):
        if edge not in used_edges:
            duplicated_complete_graph.remove_edge(edge[0], edge[1])

    return duplicated_complete_graph 

def visualize_routed_duplicated_complete_graph(G):
    """
    Given a graph object of the form returned by visualize_duplicated_complete_graph(),
    writes an html file in visualization folder.
    """
    net = Network(notebook=True, cdn_resources = 'remote')
    net.force_atlas_2based()
    net.from_nx(G)
    net.show('visualization/routed_duplicated_complete_graph_visual.html')


def reconstruct_sink_connections(G, chosen_sink_matrix, duplication_stats):
    """
    Given a graph of the form returned by add_routes(), reconstructs the sink connections
    in the graph.
    """
    # Properly book keep AP information
    counter = 1
    for i, stat in duplication_stats.items():
        for j in range(stat[0]):
            index = f'{i}.{j + 1}'
            nx.set_node_attributes(G, {counter: index}, 'title')
            counter += 1

    # Keep track of how many times each sink has been visited
    sink_dictionary = {}
    for i, edge in enumerate(copy.deepcopy(G.edges(data = True))):
        if edge[0] == 0:
            nx.set_edge_attributes(G, {(edge[0], edge[1]): 5}, 'weight')
            continue
        elif edge[1] == 0:
            sink_thru = chosen_sink_matrix[int(G.nodes[edge[0]]['title'][0])][0]
        else:
            sink_thru = chosen_sink_matrix[int(G.nodes[edge[0]]['title'][0])][int(G.nodes[edge[1]]['title'][0])]
        if sink_thru in sink_dictionary:
            sink_dictionary[sink_thru] += 1
        else:
            sink_dictionary[sink_thru] = 1
        sink_label = f'{sink_thru}.{sink_dictionary[sink_thru]}'
        G.add_node(sink_label, shape = 'image', image = 'icons/sink.png')
        new_edges = [(edge[0], sink_label), (sink_label, edge[1])]
        G.add_edges_from(new_edges, color = edge[2]['color'], weight = edge[2]['width'])
    
    return G

def visualize_reconstructed_graph(G):
    """
    Given a graph of the form returned by reconstruct_sink_connections(), writes an html file in visualization folder
    """
    net = Network(notebook=True, cdn_resources = 'remote', directed = True)
    net.force_atlas_2based()
    net.from_nx(G)
    net.show('visualization/final_reconstructed_graph.html')



#############################################################################
# SUPPORT FOR TRANSFORMING GRAPH OBJECT INTO A GRAPH THAT SOLVER RECOGNIZES #
#############################################################################

def create_instance_of_solver(G):
    """
    Given a graph of the form returned by create_graph(), transforms it into a graph 
    ready to be passed into the solver.
    """

    # Create blank adjacency matrix
    total_nodes = len(G.nodes)
    adjacency_matrix = [['INF' for j in range(total_nodes)] for i in range(total_nodes)]

    for edge in G.edges.data('title'):
        adjacency_matrix[edge[0]-1][edge[1]-1] = edge[2]

    return adjacency_matrix

if __name__ == '__main__':
    
    # CODE FOR DEMONSTRATIONS w/ VARIABLE GRAPH PARAMETERS

    num_aps = 7
    num_sinks = 5
    num_other = 23
    edges = [(1,15,2), 
             (2,14,3), (2, 19, 4), [2,22,19],
             (3,19,2), (3,17,4), (3,10,15), (3,23,1),
             (4,18,18), (4,20,3), (4,25,10),
             (5,29,12), (5,32,3), (5,33,20),
             (6,31,6), (6,28,14), (6,34,21),
             (7,29,16), (7,30,2),
             (8,15,6),
             (9,13,10), (9,17,17),
             (10,19,6),
             (11,25,2), (11,26,8), (11,24,6),
             (12,35,5),
             (13,9,10), (13,17,1),
             (14,15,2),
             (15,8, 6), (15,1,2), (15,19,1),
             (16,15,8),
             (17,16,9), (17,13,1), (17,9,17), (17,20,2),
             (18,4,18), (18,25,9),
             (19,2,4), (19,3,2),
             (20,17,2), (20,24, 7), (20,4,3),
             (21,26,2),
             (22,2,19), (22,27,8),
             (23,3,1), (23,5,6), (23,20,1),
             (24,20,7), (24,11,6), (24,29,2),
             (25,4,10), (25,26,1), (25,18, 9),
             (26,25,1), (26,21,2), (26,11,8),
             (27,22,8), (27,31,18),
             (28,10,7), (28,32,18),
             (29,24,2), (29,30,17), (29,33,8), (29,7,16),
             (30,29,17), (30,7,2),
             (31,27,18), (31,6,3), 
             (32,28,18), (32,35,4),
             (33,29,8),
             (34,6,21), (34,32,12), (34,12, 6),
             (35,12,5), (35,32,4)
             ]
    
    vehicle_capacity = 50
    people_function = lambda x: 125
    rate_function = lambda x: 2
    num_vehicles = 7

    # Create full graph
    graph_object = nx_graph(num_aps, num_sinks, num_other, edges)
    visualize_graph(graph_object)

    # Create and visualize complete graph
    solver_instance = create_instance_of_solver(graph_object)
    returned_object = vrptw_instance.create_complete_graph(solver_instance, num_aps, num_sinks, num_other)
    complete_graph_matrix, chosen_sink_matrix = returned_object[0], returned_object[1]
    complete_graph_object = nx_complete_graph(complete_graph_matrix)
    visualize_complete_graph(complete_graph_object)

    # Create and visualize duplicated complete graph
    duplicated_complete_graph = vrptw_instance.assign_time_intervals(complete_graph_matrix, people_function, rate_function, vehicle_capacity)
    duplicated_complete_graph_matrix = duplicated_complete_graph[0]
    time_windows = duplicated_complete_graph[1]
    duplication_stats = duplicated_complete_graph[2]
    duplicated_complete_graph_object = nx_duplicated_complete_graph(duplicated_complete_graph_matrix, time_windows, duplication_stats)
    visualize_duplicated_complete_graph(duplicated_complete_graph_object)

    # Solve VRPTW
    problem_instance = vrptw_solver.create_model(duplicated_complete_graph_matrix, time_windows, num_vehicles, vehicle_capacity)
    result = vrptw_solver.solve_model(problem_instance)
    solution = result.best
    routes = solution.get_routes()

    # Add routes to duplicated complete graph
    duplicated_complete_graph_with_routes_object = add_routes(duplicated_complete_graph_object, routes)
    visualize_routed_duplicated_complete_graph(duplicated_complete_graph_with_routes_object)

    # Reconstruct sinks for final output
    reconstructed_graph_object = reconstruct_sink_connections(duplicated_complete_graph_with_routes_object, chosen_sink_matrix, duplication_stats)
    visualize_reconstructed_graph(reconstructed_graph_object)





