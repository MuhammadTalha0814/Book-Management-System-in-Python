# book.py
# Authors: [Your Name]
# Emails: [Your Email]
# Spire IDs: [Your Spire ID]

class Book:
    # Constructor of the Book class
    def __init__(self):
        # Initializing an empty dictionary to store book information
        self.books = {}

    # Function to add a new book to the library
    def add_book(self, isbn, title, author, year):
        # Assert statements for input validation
        assert isinstance(isbn, str), "ISBN should be a string."
        assert isinstance(title, str), "Title should be a string."
        assert isinstance(author, str), "Author should be a string."
        assert isinstance(year, int), "Year should be an integer."
        
        # Checking if the book already exists in the library using its ISBN
        if isbn in self.books:
            return "A book with this ISBN already exists."
        else:
            # If not, add the book to the library
            self.books[isbn] = {"title": title, "author": author, "year": year}

    # Function to view details of a book
    def view_book(self, isbn):
        # Check if the book exists in the library
        if isbn in self.books:
            return self.books[isbn]
        else:
            return "Book not found."

    # Function to edit the details of a book
    def edit_book(self, isbn, title=None, author=None, year=None):
        # Check if the book exists in the library
        if isbn in self.books:
            # Update details as provided
            if title:
                self.books[isbn]['title'] = title
            if author:
                self.books[isbn]['author'] = author
            if year:
                self.books[isbn]['year'] = year
        else:
            return "Book not found."

    # Function to delete a book from the library
    def delete_book(self, isbn):
        # Check if the book exists in the library
        if isbn in self.books:
            del self.books[isbn]
        else:
            return "Book not found."
    
    # Function to display all the books in the library
    def display_all_books(self):
        # Check if the library is empty
        if not self.books:
            print("No books in the library.")
        else:
            # Iterate through each book and print its details
            for isbn, book in self.books.items():
                print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
                
    def print_all_titles(self):
    # List comprehension to print all book titles
        [print(book['title']) for book in self.books.values()]
