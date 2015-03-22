import requests
import time


with open('onramp.latlon') as f:
    for l in f:
        pl = {}
        pl['lat'], pl['lng'] = l.split()
        pl['speed']=60
        r = requests.post(
            #"http://localhost:8000/api/v1.0/my-location",
            "http://backend.mediahackday.gehekt.nl/api/v1.0/my-location",
            data=pl,
            auth=('car', 'berlin2015')
        )
        #r = requests.post(
            #"http://localhost:8000/api/v1.0/my-location",
            #data=pl,
            #auth=('admin', 'admin')
        #)
        #prev_pl = pl
        print r.text, r.status_code
        time.sleep(3)
