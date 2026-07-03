students = {}

while True:
    print("\n1.Add Student")
    print("2.Update Marks")
    print("3.Search Student")
    print("4.Display All")
    print("5.Remove Student")
    print("6.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = int(input("Enter Marks: "))

        students[roll] = {
            "name": name,
            "age": age,
            "marks": marks
        }

    elif choice == 2:
        roll = input("Enter Roll No: ")
        if roll in students:
            students[roll]["marks"] = int(input("New Marks: "))

    elif choice == 3:
        roll = input("Enter Roll No: ")
        print(students.get(roll, "Student Not Found"))

    elif choice == 4:
        for roll, details in students.items():
            print(roll, details)

    elif choice == 5:
        roll = input("Enter Roll No: ")
        students.pop(roll, None)

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")