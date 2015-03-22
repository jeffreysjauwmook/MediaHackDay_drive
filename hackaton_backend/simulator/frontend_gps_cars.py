import requests
import time


with open('onramp.latlon') as f:
    prev_pl = None
    prev_prev_pl = None
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
        print 'car', r.text, r.status_code
        print prev_pl
        if prev_pl:
            r = requests.post(
                "http://backend.mediahackday.gehekt.nl/api/v1.0/my-location",
                data=prev_pl,
                auth=('driver1', 'berlin2015')
            )
            print 'driver1', r.text, r.status_code
        prev_pl = pl
        if prev_prev_pl:
            r = requests.post(
                "http://backend.mediahackday.gehekt.nl/api/v1.0/my-location",
                data=prev_prev_pl,
                auth=('driver2', 'berlin2015')
            )
            print 'driver2', r.text, r.status_code
        prev_prev_pl = prev_pl
        time.sleep(3)
