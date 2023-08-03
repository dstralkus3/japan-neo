####### FILE FOR GIVING OUTPUT OF MODEL #######

import os
import sys
import json

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# PIP Imports
import pickle
import random
from assemblyPoints.apObject import *
import population.data_manipulation as dm
from visualization.data_visualization import *

def find_high_coverage_aps(ap_dict, tile_dict, tile_pdf_dict):
    """
    Creates an AP object that emphasizes high coverage (> 90)      
    """
    percent_covered = 0
    num_aps = len(ap_dict)

    while percent_covered < .5:
        sample = random.sample(ap_dict.keys(), random.randint(20, 30))
        new_ap_dict = {k:v for (k,v) in zip(sample, [ap_dict[ap] for ap in sample])}
        ap_obj = AssemblyPoint(new_ap_dict)
        ap_obj.assign_ap_radius(tile_dict, tile_pdf_dict)
        percent_covered = ap_obj.get_percent_covered(tile_dict, tile_pdf_dict)

    return ap_obj

if __name__ == '__main__':

    # Forcing path to be parent directory
    os.chdir(parent_dir)

    with open('./assemblyPoints/relevant_data/pickleFiles/ap_pickle.pkl', 'rb') as f:
            data_dict = pickle.load(f)
            ap_dict = data_dict['ap_dict']

    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as f:
        data_dict = pickle.load(f)
        tile_dict = data_dict['tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']

    with open('./geometry/geometries/finer_grain.json') as file:
        json_object = json.load(file)

    with open('./population/relevant_data/pickleFiles/pop_pickle.pkl', 'rb') as file:
        data_dict = pickle.load(file)
        prefecture_tile_dict = data_dict['prefecture_tile_dict']
        tile_pdf_dict = data_dict['tile_pdf_dict']
        normalized_pdf_dict = data_dict['normalized_tile_pdf_dict']

    initial_choice = {'Pocarisweat Stadium': ([134.61771, 34.16827], 0.5), 'US Consolate General Osaka-Kobe': ([135.50184, 34.69679], 0.6), 'IAI Stadium': ([138.4813, 34.98432], 0.9), 'Matsue Athletics Stadium': ([133.0639, 35.43739], 1.5), 'Ekimae Stadium': ([130.52024, 33.37167], 0.9), 'Chiyodai Baseball Stadium': ([140.74672, 41.78525], 0.7), 'Ota Athletics Stadium': ([139.39692, 36.27539], 0.6), 'Japan National Stadium': ([139.71454, 35.67782], 0), 'Kashima Football Stadium': ([140.64016, 35.99201], 0.7), 'Toyota Stadium': ([137.17091, 35.08447], 0.2)}
    ap_choice = list(initial_choice.keys())
    ap_object = AssemblyPoint(ap_dict)
    for ap, info in ap_object.ap_dict.items():
        if math.dist(info[0], (141,41)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (138.5,37.5)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (133,33)) < .8:
              ap_choice.append(ap)
        if math.dist(info[0], (138,36)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (136.5,36)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (141.5,39)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (140.5,37.6)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (131,31.7)) < .5:
              ap_choice.append(ap)
        if math.dist(info[0], (142.5, 43.4)) < .5:
              ap_choice.append(ap)

    candidate_dict = {k:v for (k,v) in zip(ap_choice, [ap_object.ap_dict[ap] for ap in ap_choice])}
    candidate_object = AssemblyPoint(candidate_dict)
    candidate_object.assign_ap_radius(tile_dict, tile_pdf_dict)
    candidate_object.ap_dict['Japan National Stadium'] = [candidate_object.ap_dict['Japan National Stadium'][0], .6]
    
    data = {'apChoice': candidate_object}
    with open('./model/pickleFiles/model_pickle.pkl', 'wb') as file:
        data_list = pickle.dump(data,file)

    plot_points_2d(tile_dict, aps = candidate_object, circles = True)



