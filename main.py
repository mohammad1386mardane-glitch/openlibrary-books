import requests


def fetch_book():
    API_URL = "https://openlibrary.org/search.json"
    params = {"q": "programing", "limit": 50}
    response = requests.get(API_URL, params=params)
    return response.json().get("docs", [])


def filter_book(books):
    filtered_books = []
    for book in books:
        year = book.get("first_publish_year")
        if year and year > 2000:
            filtered_books.append(
                {
                    "title": book.get("title"),
                    "author": ", ".join(book.get("author_name", [])),
                    "year": year,
                }
            )
    return filtered_books
