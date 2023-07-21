import pandas as pd


def generate_aps():
    """
    Reads from csv files to generate a dictionary containing assembly points as keys and lat long as vals
    """
    # Read data
    names_df = pd.read_csv('./assemblyPoints/relevant_data/assemblyPoints.csv')
    coords_df = pd.read_csv('./assemblyPoints/relevant_data/apCoords.csv')

    ap_dict = {}
    for index, row in names_df.iterrows():
        name_of_ap = row['Place']
        corresponding_row = coords_df.loc[coords_df['Location'] == name_of_ap]
        coords = corresponding_row['Latitude, Longitude'].values[0].replace(' ', '').split(',')
        flt_coords = [float(coords[0]), float(coords[1])]
        ap_dict[name_of_ap] = (flt_coords,0)

    return ap_dict

    
if __name__ == '__main__':
    print(generate_aps())
