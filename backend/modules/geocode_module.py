import requests
from geopy.geocoders import Nominatim
import json
import os
import sys

def reverse_geocode(coordinates):
    api_key = '738524a5b5c3b857060ea4b5f32b208b'#os.environ.get('POSITIONSTACK_API')
    lat, lng = [x.strip() for x in coordinates.split(',')[:2]]
    query = f'http://api.positionstack.com/v1/reverse?access_key={api_key}&query={lat},{lng}&country=IN&limit=1'

    res = requests.get(query)
    res = json.loads(res.text)

    f = open(os.devnull, 'w')
    sys.stdout = f
    print(res)
    f.close()
    sys.stdout = sys.__stdout__

    geolocator = Nominatim(user_agent='garbageTracker')
    location = geolocator.reverse(coordinates)
    location = location.raw

    address = res['data'][0]['name']
    attr = ['county', 'state_district', 'state', 'postcode']
    for prop in attr:
        try:
            address += ', ' + location['address'][prop]
        except KeyError:
            pass

    return address
