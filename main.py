import requests


def fetch_book():
    API_URL = "https://openlibrary.org/search.json"
    params = {"q": "programing", "limit": 50}
    response = requests.get(API_URL, params=params)
    return response.json().get("docs", [])
