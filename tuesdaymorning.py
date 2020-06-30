#!/usr/bin/env python3

import requests

r = requests.get('http://api.open-notify.org/iss-now.json')
issData = r.json()
def main():
    print(r.text)
    for data in issData:
        print(data, issData[data])

if __name__ == "__main__":
    main()
