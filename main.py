import requests
import csv


def fetch_book():
    API_URL = "https://openlibrary.org/search.json"
    params = {"q": "programing", "limit": 50}
    try:
        response = requests.get(API_URL, params=params)
        return response.json().get("docs", [])
    except Exception as e:
        print(f"Error: {e}")
        exit()


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


def save_to_csv(books, filename="books.csv"):
    with open(filename, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "author", "year"])
        writer.writeheader()
        writer.writerows(books)


books = fetch_book()
filtered_books = filter_book(books)
save_to_csv(filtered_books)
print("books saved succesfully")
