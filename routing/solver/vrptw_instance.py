"""Vehicles Routing Problem (VRP) with Time Windows. Code built upon Google OR-Tools VRPTW Program. """

import numpy as np
import math
import copy
from scipy.stats import gamma


#################
# ERROR CLASSES #
#################

class IntersectingSetsError():
    pass

######################################
# FUNCTIONS TO CREATE VRPTW INSTANCE #
######################################

def floydWarshall(graph):
	""" Given an adjacency list representation of a graph, returns an APSP Matrix """
	
	# Initialize static variables
	INF = 99999
	V = len(graph)

	for i in range(V):
		for j in range(V):
			if graph[i][j] == 'INF':
				graph[i][j] = INF

    # Initialize an APSP matrix
	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
   
    # Floyd Warshall
	for k in range(V):
		for i in range(V):
			for j in range(V):
				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j])
	return dist

def create_complete_graph(G, a, s, n):
    """
    Given a graph G in an adjacency matrix representation with time distances where the first a entries represent
    assembly point nodes, the next s entries represent sink nodes, and the remaining n nodes are the rest, returns 
    a complete graph containing just a depot and assembly points with edge weights carefully chosen to 
    reflect pick-up/delivery constraints. Assumes A and S are disjoint and G is strongly connected, so that the APSP
    matrix has no "INF" values.
    
    The graph returned is in adjacency matrix representation. It is a complete graph, where the 0th node denotes
    the depot and the rest denote assembly points. An edge from the depot to any AP has weight 0, while an edge from
    an AP to the depot has weight given by the distance from the AP to the nearest sink. Finally, an edge from an AP 
    to another AP (not necessarily distinct) has weight given by the minimum over the sinks of the sum of the distance
    from the pre-AP to the sink and the distance from the sink to the post-AP.
    """

    # Run Floyd Warshall to return an APSP matrix
    apsp_matrix = floydWarshall(G)

    # Initialize a complete graph consisting of a depot and the assembly points
    complete_graph = [[0 for j in range(a+1)] for i in range(a + 1)]
    chosen_sinks = [[0 for j in range(a+1)] for i in range(a + 1)]

    # Add edge weights between assembly points
    for i in range(0, a):
        for j in range(0, a):
            array = [apsp_matrix[i][k] + apsp_matrix[k][j] for k in range(a, a + s)]
            argmin = np.argmin(array)
            min_sink = a + argmin
            chosen_sinks[i + 1][j + 1] = min_sink + 1
            complete_graph[i+1][j+1] = array[argmin]


    # Add edge weights from assembly points to depot
    for i in range(0,a):
        sink_array = apsp_matrix[i][a:a+s]
        new_argmin = np.argmin(sink_array)
        minimum_sink = a + new_argmin
        complete_graph[i+1][0] = apsp_matrix[i][new_argmin]
        chosen_sinks[i+1][0] = minimum_sink + 1

    return complete_graph, chosen_sinks

def assign_time_intervals(G, f, g, capacity):
    """
    Given a graph of the form returned by create_complete_graph, a function f: {1, ..., |A| + 1} -> integers, a
    function g: {1, ..., |A| + 1} -> reals that assigns a rate of assembly to each AP, and a capacity of the 
    vehicles in the routing scheme, breaks up assembly points and assigns time intervals to each of them.
    Returns a new complete graph and a list of time intervals.
    """
    # Compute how many times each AP will be duplicated
    duplication_stats = {}
    new_size = 0
    for i in range(1, len(G)):
        num_duplications, remainder = 0,0
        total_people = f(i)
        while total_people:
            num_duplications += 1
            if total_people < capacity:
                remainder = total_people
                break
            total_people -= capacity
        new_size += num_duplications
        duplication_stats[i] = (num_duplications, remainder)
    
    # Initialize and populate new graph
    complete_graph = [[0 for i in range(new_size+1)]]
    for i, ap in enumerate(G[1:]):
        new_row = []
        new_row.append(ap[0])
        for j, dist in enumerate(ap[1:]):
            for k in range(duplication_stats[j+1][0]):
                new_row.append(copy.copy(dist))
        for j in range(duplication_stats[i+1][0]):
            complete_graph.append(copy.deepcopy(new_row))
    
    # Make diagonals nil
    for i in range(len(complete_graph)):
        complete_graph[i][i] = 0

    # Assign time intervals
    time_intervals = {0: [0,1]}
    current = 1

    for ap, stats in duplication_stats.items():

        # Assign static variables
        num_duplications, remainder, rate = stats[0], stats[1], g(ap)
        rv = gamma(capacity, rate) 
        expectation = rv.mean()
        std = math.sqrt(rv.var())

        # Handle AP's with remainders differently than those without remainders
        if remainder: 
            for i in range(1, num_duplications):
                center = expectation * i
                time_intervals[current] = [round(center - 2*std), round(center + 2*std)]
                current += 1
            
            # Assign time interval to pick up remaining people
            remainder_rv = gamma(remainder, rate)
            r_expectation, r_std = remainder_rv.mean(), math.sqrt(remainder_rv.var())
            r_center = expectation * (num_duplications - 1) + r_expectation
            time_intervals[current] = [round(r_center - 2*r_std), round(r_center + 2*r_std)]
            current += 1

        else:
            for i in range(1, num_duplications + 1):
                center = expectation * i
                time_intervals[current] = [center - std, center + std]
                current += 1

    return complete_graph, time_intervals, duplication_stats
        
if __name__ == '__main__':

    # Test cases
    graph_1 = [[0,"INF","INF","INF",10,"INF","INF"],
             ["INF",0,2,"INF",4,1,5],
             ["INF",2,0,"INF","INF","INF",7],
             ["INF","INF","INF",0,9,"INF",8],
             [10,4,"INF",9,0,"INF","INF"],
             ["INF",1,"INF","INF","INF",0,"INF"],
             ["INF",5,7,8,"INF","INF",0]
             ]
    a_1 = 4
    s_1 = 3
    n_1 = 0

    graph_2 = [[0,6,'INF','INF','INF'],
               ['INF',0,3,'INF','INF'],
               [9, 'INF', 0 , 6, 1],
               [1, 'INF', 'INF', 0, 'INF'],
               [10, 'INF', 'INF', 'INF', 0, 'INF'],
            ]
    a_2 = 3
    s_2 = 2
    n_2 = 0

    time_interval_graph = [[0,0,0,0],
                           [1,2,8,7],
                           [3,5,4,3],
                           [1,8,1,9]]
    def ap_func(i):
        if i == 1:
            return 120
        if i == 2:
            return 160
        if i == 3:
            return 100
        return 0
    
    rate_func = lambda x: 1
    capacity = 50

    # Testing
    complete_graph = assign_time_intervals(time_interval_graph, ap_func, rate_func, capacity)
    print(complete_graph[1].values())


    # ROUTING TEST

    time_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [1, 0, 7, 7, 8, 8, 8, 8, 7, 7],
       [1, 7, 0, 7, 8, 8, 8, 8, 7, 7],
       [1, 7, 7, 0, 8, 8, 8, 8, 7, 7],
       [3, 5, 5, 5, 0, 4, 4, 4, 3, 3],
       [3, 5, 5, 5, 4, 0, 4, 4, 3, 3],
       [3, 5, 5, 5, 4, 4, 0, 4, 3, 3],
       [3, 5, 5, 5, 4, 4, 4, 0, 3, 3],
       [1, 8, 8, 8, 1, 1, 1, 1, 0, 9],
       [1, 8, 8, 8, 1, 1, 1, 1, 9, 0]]

    time_windows = [(0, 1), (44, 58), (95, 109), (119, 127), (44, 58), (95, 109), (146, 160), (161, 167), (44, 58), (95, 109)]
    max_time_per_vehicle = 200
    max_wait_time = 50
    num_vehicles = 4

    #routes = vrptw_solver(time_matrix,time_windows, max_time_per_vehicle, max_wait_time, num_vehicles)
    
