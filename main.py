import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_ENDPOINT = os.environ.get("API_ENDPOINT")
LIMIT = os.environ.get("LIMIT")

def main():
    print(API_ENDPOINT)

if __name__ == "__main__":
    main()