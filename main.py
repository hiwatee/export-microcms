import os
import requests
import json
import csv
import sys
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
LIMIT = os.environ.get("LIMIT")
X_API_KEY = os.environ.get("X_API_KEY")
X_GLOBAL_DRAFT_KEY = os.environ.get("X_GLOBAL_DRAFT_KEY")

def main():
    args = sys.argv
    if len(args) == 1:
        headers = {'content-type': 'application/json', 'X-API-KEY': X_API_KEY}
    else:
        headers = {'content-type': 'application/json', 'X-API-KEY': X_API_KEY, 'X-GLOBAL-DRAFT-KEY': X_GLOBAL_DRAFT_KEY}
    res = requests.get(f"{API_ENDPOINT}?limit={LIMIT}", headers=headers)
    contents = res.json()["contents"]
    data = []
    data.append(["id","question","answer","category"])
    
    for content in contents:
        category = content["category"][0]["name"] if len(content["category"]) > 0 else ""
        row = [content["id"], content["question"], content["answer"], category]
        data.append(row)

    with open('./export.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if __name__ == "__main__":
    main()