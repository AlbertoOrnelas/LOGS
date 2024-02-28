import requests
import sys
from PyQt5 import QtWidgets, QtCore

def process_response_status(status_code, isbn_input):
    if response.status_code == 200:
        process_json_parsing(isbn_input)
    elif status_code == 404:
        return "The requested ISBN was not found. Please check the ISBN and try again."
    elif status_code >= 500:
        return "The server encountered an error. Please try again later."
    else:
        return "Failed to fetch data due to an unexpected error. Please try again."

def process_json_parsing(isbn_input):
    data = response.json()

    # Construct the book key and check if it exists in the response
    book_key = f"ISBN:{isbn_input}"
    if book_key in data:
        book_details = data[book_key]

        # Extracting book details with safe fallbacks
        title = book_details.get("title", "Title not available")
        subtitle = book_details.get("subtitle", "Subtitle not available")
        authors_list = book_details.get("authors", [])
        authors = ', '.join([author.get("name", "Author not available") for author in
                             authors_list]) if authors_list else "Author not available"
        publish_date = book_details.get("publish_date", "Publish date not available")

        # Printing out some details
        print(f"Title: {title}")
        print(f"Subtitle: {subtitle}")
        print(f"Author: {authors}")
        print(f"Publish Date: {publish_date}")
    else:
        print("No details found for the provided ISBN.")

# APPLICATION WINDOW:

# app = QtWidgets.QApplication(sys.argv)
# widget = QtWidgets.QWidget()
# widget.resize(800, 600)
# widget.setWindowTitle("This is PyQt Widget example")
# widget.show()
# exit(app.exec_())

# Prompt the user for an ISBN
isbn_input = input("Please enter an ISBN: ")

# Format the URL with the user-provided ISBN
url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn_input}&jscmd=data&format=json"

response = requests.get(url)
process_response_status(response.status_code, isbn_input)

