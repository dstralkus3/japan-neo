import geopandas
import matplotlib.pyplot as plt

def create_rail_object():
    """
    Reads from ./transportation/data to generate a mode of transportation object, which is a graph
    in an adjacency list representation.
    """
    rail_gdf = geopandas.read_file('./transportation/data/raill_jpn.dbf', encoding='latin1')
    rail_gdf.plot()
    print('im here')
    plt.show()

if __name__ == '__main':
    create_rail_object()




