import json
from book import Book

def load_books(filename):
    try:
        with open(filename, 'r') as f:
            # Check if file is not empty
            if f.read():
                # If not empty, seek to start of file and load json
                f.seek(0)
                return json.load(f)
            else:
                # If file is empty, return empty dictionary
                return {}
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump({}, f)
        return {}
    except Exception as e:
        print(f"Error loading file: {e}")
        return {}


def save_books(filename, books):
    try:
        with open(filename, 'w') as f:
            json.dump(books, f)
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    book_obj = Book()
    book_obj.books = load_books("books.json")

    while True:
        print("\n1. Add book\n2. View book\n3. Edit book\n4. Delete book\n5. Display all books\n6. Display all Titles\n7. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            try:
                year = int(input("Enter year: "))  # Cast string to int
                book_obj.add_book(isbn, title, author, year)
            except ValueError:
                print("Invalid input for year. Please try again.")
        elif choice == "2":
            isbn = input("Enter ISBN: ")
            print(book_obj.view_book(isbn))
        elif choice == "3":
            isbn = input("Enter ISBN: ")
            title = input("Enter new title (or press enter to skip): ")
            author = input("Enter new author (or press enter to skip): ")
            year_input = input("Enter new year (or press enter to skip): ")
            try:
                year = int(year_input) if year_input else None  # Cast string to int if not empty
                book_obj.edit_book(isbn, title, author, year)
            except ValueError:
                print("Invalid input for year. Please try again.")
        elif choice == "4":
            isbn = input("Enter ISBN: ")
            book_obj.delete_book(isbn)
        elif choice == "5":
            book_obj.display_all_books()
        elif choice == "6":
            book_obj.print_all_titles()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")
            
        save_books("books.json", book_obj.books)

if __name__ == "__main__":
    main()
