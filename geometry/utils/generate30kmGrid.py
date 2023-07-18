
import json

def rough_grain():
    """
    Hard code for pruning bounding box of Japan. Can definitely be refactored for abstraction.
    """
    retained = []
    with open('geometry/boundingbox.json') as f:
        f_data = json.load(f)
        for elt in f_data['features']:
            if elt['geometry']['coordinates'][0][0][0] < 132.1 or elt['geometry']['coordinates'][0][0][1] > 32.2:
                if elt['geometry']['coordinates'][0][0][0] < 142.5 or elt['geometry']['coordinates'][0][0][1] > 41.2:
                    if elt['geometry']['coordinates'][0][0][0] > 137.5 or elt['geometry']['coordinates'][0][0][1] < 38:
                        if elt['geometry']['coordinates'][0][0][0] > 139 or elt['geometry']['coordinates'][0][0][1] < 39:
                            if elt['geometry']['coordinates'][0][0][0] > 135 or elt['geometry']['coordinates'][0][0][1] < 36.5:
                                if elt['geometry']['coordinates'][0][0][0] > 132 or elt['geometry']['coordinates'][0][0][1] < 34.8:
                                        if elt['geometry']['coordinates'][0][0][0] > 131.5 or elt['geometry']['coordinates'][0][0][1] < 34.6:
                                            if elt['geometry']['coordinates'][0][0][0] < 136.5 or elt['geometry']['coordinates'][0][0][1] > 34.3:
                                                if elt['geometry']['coordinates'][0][0][0] < 146 or elt['geometry']['coordinates'][0][0][1] < 41.1:
                                                    if elt['geometry']['coordinates'][0][0][0] > 129 or elt['geometry']['coordinates'][0][0][1] < 34.1:
                                                        if elt['geometry']['coordinates'][0][0][0] > 128.5 or elt['geometry']['coordinates'][0][0][1] < 28.1:
                                                            if elt['geometry']['coordinates'][0][0][0] < 129.5 or elt['geometry']['coordinates'][0][0][1] > 27.9:
                                                                if elt['geometry']['coordinates'][0][0][0] < 130 or elt['geometry']['coordinates'][0][0][1] > 29.9:
                                                                    if elt['geometry']['coordinates'][0][0][0] < 133.3 or elt['geometry']['coordinates'][0][0][1] > 33:
                                                                        if elt['geometry']['coordinates'][0][0][0] < 141 or elt['geometry']['coordinates'][0][0][1] > 37:
                                                                            if elt['geometry']['coordinates'][0][0][0] < 142 or elt['geometry']['coordinates'][0][0][1] > 41.6:
                                                                                retained.append(elt)

if __name__ == '__main__':
    data = {"type":"FeatureCollection",
        'features': rough_grain()
    }
    with open('geometry/geometries/rough_generated.json', 'w') as f:
        json.dump(data, f)