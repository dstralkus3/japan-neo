import pickle

sink_dict = {'Haneda Airport': [139.77983, 35.54939], 'Kansai Airport': [135.23039, 34.432], 'Narita Airport': [140.39285, 35.77218], 'New Chitose Airport': [141.68068, 42.78757], 'Chubu Centrair Airport': [136.81075, 34.85736], 'Osaka Itami Airport': [135.44076, 34.79082], 'Nagasaki Airport': [129.91844, 32.91373], 'Fukuoka Airport': [130.44908, 33.58499], 'Sendai Airport': [140.92891, 38.1379], 'Kagoshima Airport': [130.71801, 31.80295], 'Kobe Airport': [135.22492, 34.63536], 'Kumamoto Airport': [130.85897, 32.83499], 'Miyazaki Airport': [131.44732, 31.8762], 'Yokohama Port': [139.64611, 35.45], 'Kobe Port': [135.22694, 34.67749], 'Tokyo Port': [139.79555, 35.61694], 'Osaka Port': [135.43489, 34.65159], 'Nagoya Port': [136.88, 35.08], 'Hakodate Port': [140.71594, 41.78532], 'Hakata Port': [130.40129, 33.60926], 'Hiroshima Port': [132.51559, 34.36183], 'Nagasaki Port': [129.86843, 32.74567], 'Kanazawa Port': [136.61549, 36.6082], 'Sasebo Port': [129.72454, 33.16165], 'Kochi Port': [133.57398, 33.50311]}

data_to_dump = {'sink_dict': sink_dict}

with open('./sinks/relevant_data/pickleFiles/sink_pickle.pkl', 'wb') as file:
        data_list = pickle.dump(data_to_dump, file)
    
