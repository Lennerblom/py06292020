#!/usr/bin/ python3
# Author: Michael
#import argparse
import webbrowser
import requests

# finding the location of an entered IP address
def main():
    URL = 'http://ip-api.com/json/'
    ip = str(input("Please enter an IP address, format is 12.34.5.6\n"))
    print(URL + ip)
    newURL = f"{URL}{ip}"
    req = requests.get(newURL)
    data = req.json()
    city = data["city"]
    country = data['country']
    with open('locations.txt', 'w') as f:
        print(f'{city}\n{country}', file=f)
    #lat = data["lat"]
    #lon = data["lon"]

    webbrowser.open(newURL)

if __name__ == "__main__":
    main()
