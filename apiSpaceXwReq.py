#!/usr/bin/ python3

# using std library method for getting at API data
# import urllib.request
# import json
import requests

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    # coreData = urllib.request.urlopen(SPACEXURI)
    coreData = requests.get(SPACEXURI)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    #xString = coreData.read().decode()
    #print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    #listOfCores = json.loads(xString)
    listOfCores = coreData.json()
    #print(type(listOfCores))

    for core in listOfCores:
       # print(core, end="\n\n")
        print("The core serial is: ", core["core_serial"])
        print("The original launch date of: ", core['original_launch'])
        if core['missions']:
            print('the missions were:')
            for mission in core['missions']:
                print(f"  {mission['name']}")
        print("\n")

if __name__ == "__main__":
    main()
