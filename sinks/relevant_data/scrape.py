
import sys
import os
import pandas as pd

# Append system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

def get_sinks():
    """
    Scrapes files to get sink dictionary
    """
    sinks_df = pd.read_csv('./sinks/relevant_data/sinks.csv')
    sink_dict = {}
    for index, row in sinks_df.iterrows():
        location = row['Location']
        if 'Port' in location or 'Airport' in location:
            coords = row['Latitude, Longitude'].replace(' ', '').split(',')
            flt_coords = [float(coords[1]), float(coords[0])]
            sink_dict[location] = flt_coords
    
    return sink_dict


if __name__ == '__main__':
    pass
