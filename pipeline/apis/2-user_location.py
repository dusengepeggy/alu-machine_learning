#!/usr/bin/env python3
"""Print the location of a GitHub user given the API URL as an argument."""

import requests
import sys
import time


if __name__ == "__main__":
    res = requests.get(sys.argv[1])

    if res.status_code == 403:
        reset = int(res.headers.get('X-Ratelimit-Reset'))
        minutes = round((reset - int(time.time())) / 60)
        print("Reset in {} min".format(minutes))
    elif res.status_code == 404:
        print("Not found")
    elif res.status_code == 200:
        print(res.json().get('location'))