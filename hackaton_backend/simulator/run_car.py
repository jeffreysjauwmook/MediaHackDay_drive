import requests
import time
import datetime
import random

distance = 5

heavy = False
km_total = 0

old = 0
counter = 0 
lock = False
heavy = 'false'

while True:
    if not lock:
        rnd = random.getrandbits(1)
    if rnd == old and counter < 5:
        print "locked"
        lock = True
        counter += 1
        heavy = old
    else:
        print "new"
        lock = False
        old = rnd
        counter = 0
        heavy = rnd
    print heavy
    ts =time.time()
    d = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%S')
    payload = {'vim': '123', 'km_total': km_total, 'heavy': heavy, 'fuel_diff': 0, 'fuel_total': 0, 'timestamp' : d}
    r = requests.post("http://backend.mediahackday.gehekt.nl/as-api/v1.0/entry", data=payload)
    print r.text
    time.sleep(1)

for i in range(0,distance):
    if (i < 2):
        heavy = 'false'
    if (i >= 2 and i < 3):
        heavy = 'true'
    if (i >= 3):
        heavy = 'false'
    km_total+=i
    # YYY-MM-DDThh:mm[:s

    #r = requests.post("http://localhost:8000/as-api/v1.0/entry", data=payload)
    print r.text
    time.sleep(60)
