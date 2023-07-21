
import math
import time
import pickle


def ap_influence(tile_dictionary, coordinates, radius):
    """"
    Given a tile dictionary, which contains indices as keys and lat lon as values, coordinates of the 
    assembly point, and radius of coverage of the assembly point, returns a set of indices that the assembly point
    reaches
    """
    touches = set()
    for key,val in tile_dictionary.items():

        if math.sqrt((val[0] - float(coordinates[1]))**2 + (val[1] - float(coordinates[0]))**2) < radius:
            touches.add(key)
    return touches

def choose_aps(feasible_aps, tile_dict, tile_pdf_dict, radius):
    """
    Given a dictionary of names of feasible aps as keys and coordinates as values, a tile_dict of the form
    returned by create_tile_dictionary in population/data_manipulation, a tile_pdf_dict of the form 
    returned by generateDistribution in population/data_manipulation.py, and a radius, chooses a subset of the feasible ap's
    to act as assembly points during the NEO.
    """
    # First, check that it is possible to cover the pdf with the given feasibles and radius
    total_people = sum(tile_pdf_dict.values())
    total_covered = set()
    for ap, coords in feasible_aps.items():
        containing_set = ap_influence(tile_dict, coords, radius)
        total_covered = total_covered.union(containing_set)

    covered = 0
    for tile in total_covered:
        covered += tile_pdf_dict[tile]
    print(covered/total_people)
    return total_covered

if __name__ == '__main__':

    # Load relevant data
    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        tile_dict = data_dict['tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']
    
    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']

    total_covered = choose_aps(ap_dict, tile_dict, tile_pdf_dict, 1.8)


    