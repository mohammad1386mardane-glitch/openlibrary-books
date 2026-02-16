import requests
import csv
from typing import List, Dict, Any


def fetch_book() -> List[Dict[str, Any]]:
    API_URL: str = "https://openlibrary.org/search.json"
    params: Dict[str, Any] = {"q": "programming", "limit": 50}

    try:
        response: requests.Response = requests.get(API_URL, params=params)
        response.raise_for_status()

        data: Dict[str, Any] = response.json()
        return data.get("docs", [])

    except requests.RequestException as e:
        print(f"Error: {e}")
        exit()


def filter_book(books: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    filtered_books: List[Dict[str, Any]] = []

    for book in books:
        year: Any = book.get("first_publish_year")

        if isinstance(year, int) and year > 2000:
            filtered_books.append(
                {
                    "title": book.get("title", "Unknown"),
                    "author": ", ".join(book.get("author_name", [])),
                    "year": year,
                }
            )

    return filtered_books


def save_to_csv(books: List[Dict[str, Any]], filename: str = "books.csv") -> None:

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(books)


books: List[Dict[str, Any]] = fetch_book()
filtered_books: List[Dict[str, Any]] = filter_book(books)
save_to_csv(filtered_books)
print("Books saved successfully")
