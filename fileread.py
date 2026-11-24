import vt
import hashlib
import os
api_key = open("api_key.txt")
client = vt.Client(api_key.read())
shash = hashlib.new("SHA256")
def fhash(path): #hashprint command
    filepath = path
    with open (filepath, "rb") as f:
        bytes = f.read()
        shash.update(bytes)
        print(fhash.hexdigest())
    #reads file bytes
    #obtains hash
    #sends hash to vt-py using client.get_object()
    #extra arguments could be submitted to read stats. 

def filescan(path):
    filepath = path
    with open(filepath, "rb") as f:
        analyze = client.scan_file(f, wait_for_completion=True)
        analysis = client.get_object("/analyses/" + analyze.id)
        statistics = analysis.stats
        for i in statistics:
            print(f"{i}: {statistics[i]}")
        client.close()

def hashscan(shash):
    sample = shash
    f = client.get_object("/files/" + sample)
    statistics = f.last_analysis_stats
    for i in statistics:
        print(f"{i}: {statistics[i]}")
        client.close()
