#!/usr/bin/env python3

import requests
from geopy.geocoders import Nominatim

r = requests.get('http://api.open-notify.org/iss-now.json')
issData = r.json()
def main():
    print(r.text)
    for data in issData:
        print(data, issData[data])

    message = issData['message']
    print("the message back is", message)

    location = geolocator.reverse(issData["iss_position"]["longitude"] + "," +issData["iss_position"]["latitude"] )

    print("the location is at: ", location)

if __name__ == "__main__":
    main()
