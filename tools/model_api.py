import sys
sys.path.append("..")

import requests


URL = "https://pmmpublisher.pps.eosdis.nasa.gov/opensearch?q=global_landslide_nowcast_3hr&lat=0&lon=0&limit=1&startTime=2000-10-2&endTime=2021-10-2"
r = requests.get(url = URL)
data = r.json()

URL = data["items"][0]["action"][0]["using"][5]["using"][0]["url"]
r = requests.get(url = URL)
data = r.json()

#TODO load in database
