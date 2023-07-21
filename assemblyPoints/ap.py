
import math
import time
import pickle
import heapq

def ap_influence(tile_dictionary, coordinates, radius):
    """"
    Given a tile dictionary, which contains indices as keys and lat lon as values, coordinates of the 
    assembly point, and radius of coverage of the assembly point, returns a set of indices that the assembly point
    reaches
    """
    touches = set()
    for key,val in tile_dictionary.items():

        if math.sqrt((val[0] - coordinates[1])**2 + (val[1] - coordinates[0])**2) < radius:
            touches.add(key)
    return touches

def assign_ap_radius(ap_dictionary, tile_dict, tile_pdf_dict):
    """
    Given a dictionary with names of aps as keys and coordinates as values, a tile_dict of the form
    returned by create_tile_dictionary in population/data_manipulation, a tile_pdf_dict of the form 
    returned by generateDistribution in population/data_manipulation.py, and a radius, chooses a subset of the feasible ap's
    to act as assembly points during the NEO.
    """
    ap_dict = ap_dictionary.copy()

    # Static variables
    total_people = sum(tile_pdf_dict.values())

    # # For each AP, calculate a dictionary with radii as keys and tile influence as values
    ap_radius_dictionary = {}
    for ap, coords in ap_dict.items():
        ap_radius_dictionary[ap] = {}
        radius = 0
        percent_covered = 0
        while percent_covered < .999:
            tiles_covered = ap_influence(tile_dict, coords[0], radius)
            ap_radius_dictionary[ap][round(radius,1)] = tiles_covered
            covered = sum([tile_pdf_dict[tile] for tile in tiles_covered])
            percent_covered = covered/total_people
            radius += .1
    
    # # Set radii to 0 and initialize min heap of cost of decrementing radius
    # heap = []
    # for ap in ap_dict:
    #     covered_after = ap_radius_dictionary[ap][.1]
    #     people_covered_after = sum([tile_pdf_dict[tile] for tile in covered_after])
    #     difference = round(people_covered_after,2)
    #     heap.append((-difference, ap))

    # Increment until the pdf is no longer covered
    # percent_covered = 0
    # total_tiles_covered = set()

    # while percent_covered < .9:

    #     to_increment = heapq.heappop(heap)
    #     # Change radius
    #     name_of_ap = to_increment[1]
        
    #     current = (ap_dict[name_of_ap][0], ap_dict[name_of_ap][1])
    #     new = (current[0], round(current[1] + .1, 1))
    #     ap_dict[name_of_ap] = new

    #     # Re-calculate coverage
    #     tiles_covered = get_tiles_covered(tile_dict, ap_dict)
    #     total_tiles_covered = total_tiles_covered.union(tiles_covered)
    #     people_covered = sum([tile_pdf_dict[tile] for tile in tiles_covered])
    #     percent_covered = people_covered / total_people

    #     # Push to heap
    #     covering_next = ap_radius_dictionary[ap][round(new[1] + .1, 1)]
    #     newly_covered = covering_next.difference(total_tiles_covered)
    #     overlap = len(newly_covered)/len(covering_next)

    #     benefit = sum([tile_pdf_dict[tile] for tile in covering_next])

    #     if benefit != 0:
    #         heapq.heappush(heap,(-(overlap/benefit), name_of_ap))
    #     else:
    #         heapq.heappush(heap,(-overlap, name_of_ap))
    
    to_check = ap_dict.keys()
    total_tiles_covered = set()
    while to_check:
        next_round = []
        for ap in to_check:
            # Increment radius by .1 if it doesn't intersect anything
            current_radius = ap_dict[ap][1]
            next_radius = round(current_radius + .1, 1)
            if ap_radius_dictionary[ap][next_radius].difference(ap_radius_dictionary[ap][current_radius]).intersection(total_tiles_covered):
                continue
            else:
                ap_dict[ap] = (ap_dict[ap][0], next_radius)
                total_tiles_covered = total_tiles_covered.union(ap_radius_dictionary[ap][next_radius])
                next_round.append(ap)
        to_check = next_round
    
    # Calculate percent covered
    tiles_covered = get_tiles_covered(tile_dict, ap_dict)
    total_tiles_covered = total_tiles_covered.union(tiles_covered)
    people_covered = sum([tile_pdf_dict[tile] for tile in tiles_covered])
    percent_covered = people_covered / total_people
    return ap_dict, percent_covered

def get_tiles_covered(tile_dict, ap_dict):
    """
    Given a tile dictionary and an ap_dict of the form returned by generate_aps() in scrape.py,
    calculates the tiles covered
    """
    tiles_covered = set()
    for ap, val in ap_dict.items():
        ap_coords = val[0]
        ap_rad = val[1]
        for tile, tile_coords in tile_dict.items():
            if math.sqrt((ap_coords[1] - tile_coords[0])**2 + (ap_coords[0] - tile_coords[1])**2) < ap_rad:
                tiles_covered.add(tile)
            
    return tiles_covered


if __name__ == '__main__':

    # Load relevant data
    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        tile_dict = data_dict['tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']
    
    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        ap_dict = data_dict['ap_dict']

    assign_ap_radius(ap_dict, tile_dict, tile_pdf_dict)

    