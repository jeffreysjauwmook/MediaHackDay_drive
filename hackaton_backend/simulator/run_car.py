import requests
import time
import datetime

distance = 5

heavy = False
km_total = 0

for i in range(0,distance):
    if (i < 2):
        heavy = False
    if (i >= 2 and i < 3):
        heavy = True
    if (i >= 3):
        heavy = False
    km_total+=i
    # YYY-MM-DDThh:mm[:s
    ts =time.time()
    d = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%S')
    print d
    #{"timestamp":["This field is required."],"fuel_diff":["This field is required."],"fuel_total":["This field is required."]}
    payload = {'vim': '123', 'km_total': km_total, 'heavy': heavy, 'fuel_diff': 0, 'fuel_total': 0, 'timestamp' : d}

    r = requests.post("http://backend.mediahackday.gehekt.nl/as-api/v1.0/entry", data=payload)
#    r = requests.post("http://localhost:8000/as-api/v1.0/entry", data=payload)
    print r.text
