# Student Management System

# Dictionary to store all student records
students = {}

# Function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"

# Function to display menu
def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

# Function to add a new student
def add_student():
    try:
        # Taking roll number input
        roll = int(input("Enter Roll Number: "))

        # Prevent duplicate roll numbers
        if roll in students:
            print("Roll Number already exists!")
            return

        # String operation using strip() and title()
        name = input("Enter Student Name: ").strip().title()

        # List to store marks of 5 subjects
        marks = []

        # Loop to take marks input
        for i in range(1, 6):
            mark = float(input(f"Enter Marks of Subject {i}: "))
            marks.append(mark)

        # Calculate percentage
        percentage = sum(marks) / 5

        # Calculate grade using function
        grade = calculate_grade(percentage)

        # Store data in dictionary
        students[roll] = {
            "Name": name,
            "Marks": marks,
            "Percentage": percentage,
            "Grade": grade
        }

        print("Record Added Successfully!")

    except ValueError:
        # Exception handling for invalid input
        print("Invalid Input!")

# Function to display all students
def view_all():
    if len(students) == 0:
        print("No Records Found!")
    else:
        for roll, details in students.items():
            print("\nRoll Number :", roll)
            print("Name :", details["Name"])
            print("Marks :", details["Marks"])
            print("Percentage :", round(details["Percentage"], 2))
            print("Grade :", details["Grade"])

# Function to search student by roll number
def search_student():
    try:
        roll = int(input("Enter Roll Number to Search: "))

        if roll in students:
            details = students[roll]

            print("Name :", details["Name"])
            print("Marks :", details["Marks"])
            print("Percentage :", round(details["Percentage"], 2))
            print("Grade :", details["Grade"])
        else:
            print("Student Not Found!")

    except ValueError:
        print("Invalid Input!")

# Function to update student record
def update_student():
    try:
        roll = int(input("Enter Roll Number to Update: "))

        if roll in students:
            name = input("Enter New Name: ").strip().title()

            marks = []

            # Loop to update marks
            for i in range(1, 6):
                mark = float(input(f"Enter New Marks of Subject {i}: "))
                marks.append(mark)

            percentage = sum(marks) / 5
            grade = calculate_grade(percentage)

            students[roll] = {
                "Name": name,
                "Marks": marks,
                "Percentage": percentage,
                "Grade": grade
            }

            print("Record Updated Successfully!")

        else:
            print("Student Not Found!")

    except ValueError:
        print("Invalid Input!")

# Function to delete student record
def delete_student():
    try:
        roll = int(input("Enter Roll Number to Delete: "))

        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found!")

    except ValueError:
        print("Invalid Input!")

# Main program loop
while True:

    # Display menu
    show_menu()

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_all()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Numbers Only!")