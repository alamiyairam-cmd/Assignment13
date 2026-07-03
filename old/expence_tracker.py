# Personal Expense Tracker

# List to store expenses
expenses = []

# Function to add expense
def add_expense():
    try:
        # Taking input from user
        description = input("Enter Description: ").strip().title()
        category = input("Enter Category: ").strip().title()
        amount = float(input("Enter Amount: "))

        # Check amount
        if amount <= 0:
            print("Invalid Amount!")
            return

        # Store data in dictionary
        expense = {
            "Description": description,
            "Category": category,
            "Amount": amount
        }

        # Add dictionary to list
        expenses.append(expense)

        print("Expense Added Successfully!")

    except ValueError:
        # Handle invalid amount
        print("Invalid Input!")

# Function to view expenses
def view_expenses():

    if len(expenses) == 0:
        print("No Expenses Found!")

    else:
        print("\nExpense List")

        # Using for loop
        for expense in expenses:
            print(expense)

# Function to show category summary
def category_summary():

    summary = {}

    # Calculate category-wise total
    for expense in expenses:

        category = expense["Category"]

        if category in summary:
            summary[category] += expense["Amount"]
        else:
            summary[category] = expense["Amount"]

    print("\nCategory Summary")

    for category, total in summary.items():
        print(category, ":", total)

# Main Program
budget = float(input("Enter Monthly Budget: "))

while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            category_summary()

        elif choice == 4:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        # Exception handling
        print("Please Enter Numbers Only!")