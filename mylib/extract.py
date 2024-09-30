"""
Extract a dataset from a URL within github. In this case we are looking at soccer data
"""
import requests
import os

def extract(url="https://raw.githubusercontent.com/footballcsv/england/refs/heads/master/2010s/2010-11/eng.1.csv", 
            file_path="data/match_results.csv"):
    if not os.path.exists("data"):
        os.makedirs("data")
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path