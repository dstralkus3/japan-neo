###########
# IMPORTS #
###########

from pyvrp.stop import MaxRuntime
from pyvrp import Model

def create_model(G, time_windows, num_vehicles, capacity):
    """
    From the graph and time_windows returned from assign_time_intervals in solver/vrptw_instance.py, creates a model
    instance of the PyVRP module.
    """
    # Initialize model and pointer dictionary
    pyvrp_instance = Model()
    client_dictionary = {}

    # Add depot and assembly points
    client_dictionary[0] = pyvrp_instance.add_depot(0,0,time_windows[0][0],time_windows[0][1]) 

    for i in range(1,len(G)):
        client_dictionary[i] =  pyvrp_instance.add_client(0,0, 0, 0, time_windows[i][0], time_windows[i][1])

    # Add edges
    for i in range(len(G)):
        for j in range(len(G)):
            pyvrp_instance.add_edge(client_dictionary[i], client_dictionary[j], G[i][j], G[i][j])

    # Add vehicle type
    pyvrp_instance.add_vehicle_type(capacity, num_available= num_vehicles)

    return pyvrp_instance

def solve_model(instance):
    """
    Given an instance returned by create_model(), solves for routes
    """
    result_object = instance.solve(MaxRuntime(5))                         
    return result_object
    


    

        
