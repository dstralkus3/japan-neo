import json
import numpy as np

new = []

with open("geometry/geometries/rougher_grain.json") as f:
    json_data = json.load(f)
    for elt in json_data['features']:
        coordinates = elt['geometry']['coordinates'][0]

        # Define vertices of new squares
        bottom_left, top_left, top_right, bottom_right = coordinates[0], coordinates[1],coordinates[2],coordinates[3]
        mid_left = (bottom_left[0], (bottom_left[1] + top_left[1])/2)
        mid_top = ((top_left[0] + top_right[0])/2, top_left[1])
        mid_right =  (top_right[0], (top_right[1] + bottom_right[1])/2)
        mid_bottom = ((bottom_right[0] + bottom_left[0])/2, bottom_left[1])
        center = (mid_bottom[0], mid_left[1])

        # Define squares
        square_1 = [bottom_left, mid_left, center, mid_bottom, bottom_left]
        square_2 = [mid_left, top_left, mid_top, center, mid_left]
        square_3 = [center, mid_top, top_right, mid_right, center]
        square_4 = [mid_bottom, center, mid_right, bottom_right, mid_bottom]

        # Append new tiles
        for square in [square_1, square_2, square_3, square_4]:
            new.append({
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": [square],
            "type": "Polygon"
            }
            })


data = {"type":"FeatureCollection",
    'features': new
}

with open('geometry/geometries/fine_generated.json', 'w') as f:
    json.dump(data, f)