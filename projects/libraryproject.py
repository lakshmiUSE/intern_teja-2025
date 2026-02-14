# Library Book Management System

books = []
book_id_counter = 1

# Function to add a book
def add_book():
    global book_id_counter
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    book = {
        "id": book_id_counter,
        "title": title,
        "author": author,
        "status": "available"
    }
    books.append(book)
    book_id_counter += 1
    print("Book added successfully!\n")

# Function to view books
def view_books():
    if not books:
        print("No books available.\n")
        return

    print("\n--- Library Books ---")
    for book in books:
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")
    print()

# Function to issue book
def issue_book():
    book_id = int(input("Enter book ID to issue: "))

    for book in books:
        if book['id'] == book_id:
            if book['status'] == "issued":
                print("Book is already issued!\n")
            else:
                book['status'] = "issued"
                print("Book issued successfully!\n")
            return
    print("Book ID not found!\n")

# Function to return book
def return_book():
    book_id = int(input("Enter book ID to return: "))

    for book in books:
        if book['id'] == book_id:
            if book['status'] == "available":
                print("Book is already available in library!\n")
            else:
                book['status'] = "available"
                print("Book returned successfully!\n")
            return
    print("Book ID not found!\n")

# Function to search book by title
def search_book():
    search_title = input("Enter book title to search: ").lower()

    found = False
    for book in books:
        if search_title in book['title'].lower():
            print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")
            found = True

    if not found:
        print("No matching book found!\n")

# Function to remove book
def remove_book():
    book_id = int(input("Enter book ID to delete: "))

    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            print("Book deleted successfully!\n")
            return

    print("Book ID not found!\n")

# Main Program Loop
while True:
    print("""
======== LIBRARY MANAGEMENT ========
1. Add Book
2. View All Books
3. Issue Book
4. Return Book
5. Search Book by Title
6. Remove/Delete Book
7. Exit Program
====================================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        remove_book()
    elif choice == "7":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, try again!\n")