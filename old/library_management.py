# ==============================
# LIBRARY MANAGEMENT SYSTEM
# ==============================

# Import module to calculate due date
from datetime import datetime, timedelta

# Nested dictionary to store books
library = {}

# Function to display menu
def show_menu():
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")


# Function to add a new book
def add_book():
    try:
        # Taking book details from user
        isbn = input("Enter ISBN Number: ").strip()

        # Check duplicate ISBN
        if isbn in library:
            print("Book already exists!")
            return

        title = input("Enter Book Title: ").strip().title()
        author = input("Enter Author Name: ").strip().title()

        # Store data in nested dictionary
        library[isbn] = {
            "title": title,
            "author": author,
            "available": True,
            "borrower": None,
            "issue_date": None
        }

        print("Book Added Successfully!")

    except ValueError:
        print("Invalid Input!")


# Function to issue book
def issue_book():
    try:
        isbn = input("Enter ISBN Number: ").strip()

        # Check if book exists
        if isbn in library:

            # Check availability
            if library[isbn]["available"]:

                borrower = input("Enter Borrower Name: ").strip().title()
                student_id = input("Enter Student ID: ").strip().upper()

                # Store issue date
                issue_date = datetime.now()

                # Due date after 7 days
                due_date = issue_date + timedelta(days=7)

                library[isbn]["available"] = False
                library[isbn]["borrower"] = borrower
                library[isbn]["student_id"] = student_id
                library[isbn]["issue_date"] = issue_date

                print("\nBook Issued Successfully!")
                print("Title :", library[isbn]["title"])
                print("Due Date :", due_date.strftime("%d-%m-%Y"))

            else:
                print("Book Already Issued!")

        else:
            print("Book Not Found!")

    except KeyError:
        print("Invalid ISBN!")


# Function to return book
def return_book():
    try:
        isbn = input("Enter ISBN Number: ").strip()

        if isbn in library:

            if not library[isbn]["available"]:

                # Change status after return
                library[isbn]["available"] = True
                library[isbn]["borrower"] = None
                library[isbn]["issue_date"] = None

                print("Book Returned Successfully!")

            else:
                print("Book is already available.")

        else:
            print("Book Not Found!")

    except KeyError:
        print("Invalid ISBN!")


# Function to search book by title or author
def search_book():
    keyword = input("Enter Title or Author Name: ").strip().lower()

    found = False

    # Loop through dictionary
    for isbn, details in library.items():

        # String operation using find()
        if details["title"].lower().find(keyword) != -1 or details["author"].lower().find(keyword) != -1:

            print("\nISBN :", isbn)
            print("Title :", details["title"])
            print("Author :", details["author"])

            if details["available"]:
                print("Status : Available")
            else:
                print("Status : Issued")

            found = True

    if not found:
        print("Book Not Found!")


# Function to display all books
def view_catalog():

    if len(library) == 0:
        print("No Books Available!")

    else:
        print("\n===== BOOK CATALOG =====")

        for isbn, details in library.items():

            print("\nISBN :", isbn)
            print("Title :", details["title"])
            print("Author :", details["author"])

            if details["available"]:
                print("Status : Available")
            else:
                print("Status : Issued")


# Main program using while loop
while True:

    # Display menu
    show_menu()

    try:
        choice = int(input("Enter Choice : "))

        if choice == 1:
            add_book()

        elif choice == 2:
            issue_book()

        elif choice == 3:
            return_book()

        elif choice == 4:
            search_book()

        elif choice == 5:
            view_catalog()

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        # Exception handling
        print("Please Enter Numbers Only!")