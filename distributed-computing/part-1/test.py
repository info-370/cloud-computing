import requests as r
import threading

cities = ["baltimore", "charleston", "chicago", "columbus", "dayton",
          "denver", "kc", "memphis", "milwaukee", "ok_city", "pittsburgh",
          "st_louis", "syracuse", "wichita"]

def get_avg(c):
    res = r.get('http://localhost:5000/average_pop?city=' + c)
    print(c + " average population: " + res.text)

for c in cities:
    threading.Thread(target=get_avg, args=(c,)).start()
