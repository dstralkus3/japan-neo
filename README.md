This is a repository for the construction of a NEO in Japan

The geometry folder contains files to simplify Japan's geometry for better computer representation. The sub-folder utils contains functions
used to create the geometric representation while the geometries sub-folders contain the actual geometries. Within the geometries sub-folder, finer_grain.json and rougher_grain.json contain the actual representations of Japan.

The population folder contains files to populate the discretized geometry with a population density function. This includes
necessary data manipulation and visualization tools. Furthermore, the relevant_data folder contains logic to scrape information from
the web and pickle that data so the data_manipulation.py and data_visualization.py files are abstracted from it.

The routing folder contains logic to route vehicles.

The assembly point folder contains logic that draws from the population folder to choose assembly points.

Dependencies:
- pyvrp
- matplotlib
- mpl_toolkits
- numpy
- reverse_geocode
- Beautiful soup
- Json
- Requests
- geopy
- pickle
- math
- pandas
- time
- geopandas
- haverstine





