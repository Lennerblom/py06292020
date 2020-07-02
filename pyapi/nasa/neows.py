#!/usr/bin/ python3
from dotenv import load_dotenv
load_dotenv()
import os
SECRET_KEY = os.getenv("NASA")
import requests
## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first I want to grab my credentials
   # with open("/home/student/nasa.creds", "r") as mycreds:
    #    nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + SECRET_KEY        

    ## update the date below, if you like
    startdate = "start_date=2019-11-11"
    
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
    
    # strip off json attachment from our response
    neodata = neowrequest.json()
        
    ## display NASAs NEOW data
    print(neodata)
    
if __name__ == "__main__":
    main()


