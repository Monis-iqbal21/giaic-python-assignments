import json
import os

BOOKS_FILE = 'library.json'

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_books(books):
    with open(BOOKS_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def add_book(books):
    title = input("Book Title: ")
    author = input("Book Author: ")
    try:
        publication_year = int(input("Publication Year: "))
    except ValueError:
        print("Invalid year! Please enter a number.")
        return
    genre = input("Genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = read_input == 'yes'

    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status
    }
    books.append(book)
    print("✅ Book added successfully!")

def remove_book(books):
    title = input("Enter the title of the book to remove: ").strip()
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found!")

def search_book(books):
    keyword = input("Enter title or author to search: ").strip().lower()
    found = False
    for book in books:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print_book(book)
            found = True
    if not found:
        print("❌ No matching books found!")

def print_book(book):
    print(f"\nTitle: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['publication_year']}")
    print(f"Genre: {book['genre']}")
    print(f"Read: {'Yes' if book['read_status'] else 'No'}")

def display_all_books(books):
    if not books:
        print("📚 Your library is empty.")
    else:
        for book in books:
            print_book(book)

def display_stats(books):
    total = len(books)
    read = sum(1 for book in books if book["read_status"])
    if total == 0:
        print("📊 No books in the library.")
    else:
        print(f"Total Books: {total}")
        print(f"Books Read: {read}")
        print(f"Read Percentage: {read / total * 100:.2f}%")

def main():
    books = load_books()

    while True:
        print("\n📚 Personal Library Manager")
        print("#" * 40)
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            remove_book(books)
        elif choice == '3':
            search_book(books)
        elif choice == '4':
            display_all_books(books)
        elif choice == '5':
            display_stats(books)
        elif choice == '6':
            save_books(books)
            print("👋 Goodbye! Your library has been saved.")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
