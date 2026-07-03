# ===============================
# INVENTORY MANAGEMENT SYSTEM
# ===============================

# Dictionary to store products
inventory = {}

# List to store transactions
transactions = []

# Set to store unique categories
categories = set()

# Function to add product
def add_product():
    try:
        # Taking input from user
        product_id = input("Enter Product ID: ").strip().upper()

        # Check duplicate ID
        if product_id in inventory:
            print("Product ID already exists!")
            return

        name = input("Enter Product Name: ").strip().title()
        category = input("Enter Category: ").strip().title()
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        reorder_level = int(input("Enter Reorder Level: "))

        # Add category to set
        categories.add(category)

        # Store product details in dictionary
        inventory[product_id] = {
            "Name": name,
            "Category": category,
            "Price": price,
            "Quantity": quantity,
            "Reorder": reorder_level
        }

        print("Product Added Successfully!")

    except ValueError:
        # Exception handling
        print("Invalid Input!")

# Function to stock in
def stock_in():
    product_id = input("Enter Product ID: ").strip().upper()

    if product_id in inventory:

        qty = int(input("Enter Quantity to Add: "))

        inventory[product_id]["Quantity"] += qty

        # Store transaction in list
        transactions.append(("IN", product_id, qty))

        print("Stock Updated Successfully!")

    else:
        print("Product Not Found!")

# Function to stock out
def stock_out():
    product_id = input("Enter Product ID: ").strip().upper()

    if product_id in inventory:

        qty = int(input("Enter Quantity to Remove: "))

        # Prevent negative stock
        if qty <= inventory[product_id]["Quantity"]:

            inventory[product_id]["Quantity"] -= qty

            transactions.append(("OUT", product_id, qty))

            print("Stock Removed Successfully!")

        else:
            print("Not Enough Stock!")

    else:
        print("Product Not Found!")

# Function to view inventory
def view_inventory():

    if len(inventory) == 0:
        print("No Products Available!")

    else:
        print("\n===== INVENTORY =====")

        # Using for loop
        for pid, details in inventory.items():

            print("\nProduct ID :", pid)
            print("Name :", details["Name"])
            print("Category :", details["Category"])
            print("Price :", details["Price"])
            print("Quantity :", details["Quantity"])

# Function for low stock alert
def low_stock_alert():

    print("\n===== LOW STOCK ITEMS =====")

    found = False

    for pid, details in inventory.items():

        # Conditional statement
        if details["Quantity"] <= details["Reorder"]:

            print(pid, "-", details["Name"])

            found = True

    if not found:
        print("No Low Stock Products!")

# Function to generate report
def generate_report():

    total_value = 0

    # Arithmetic operation
    for details in inventory.values():
        total_value += details["Price"] * details["Quantity"]

    print("\n===== INVENTORY REPORT =====")
    print("Total Products :", len(inventory))
    print("Categories :", categories)
    print("Total Stock Value :", total_value)

# Main Program
while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_product()

        elif choice == 2:
            stock_in()

        elif choice == 3:
            stock_out()

        elif choice == 4:
            view_inventory()

        elif choice == 5:
            low_stock_alert()

        elif choice == 6:
            generate_report()

        elif choice == 7:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Numbers Only!")