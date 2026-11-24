import vt
import hashlib
import os
api_key = open("api_key.txt")
client = vt.Client(api_key.read())

def urlscan(url):
    link = url
    analysis = client.scan_url(url=url, wait_for_completion = True)
    statistics = analysis.stats
    for i in statistics:
        print(f"{i}: {statistics[i]}")
    client.close()