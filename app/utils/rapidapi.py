import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_URL = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"
RAPIDAPI_HEADERS = {
	"x-rapidapi-key": os.getenv("X_RAPIDAPI_KEY"),
	"x-rapidapi-host": os.getenv("X_RAPIDAPI_HOST")
}

def fetch_funds(fund_family: str):
    params = {"Mutual_Fund_Family": fund_family, "Scheme_Type":"Open"}
    response = requests.get(RAPIDAPI_URL, headers=RAPIDAPI_HEADERS, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch funds")
    return response.json()
