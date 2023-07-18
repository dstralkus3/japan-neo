
import reverse_geocode

def get_prefecture(latitude, longitude):
    location = reverse_geocode.get((latitude, longitude))
    if location['country_code'] == 'JP':
        return location['admin1']
    else:
        return 'Not in Japan'