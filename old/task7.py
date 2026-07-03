# Q10 - Student Club Registration

students = set()

# Input names of students
for i in range(8):
    name = input("Enter student name: ")
    students.add(name)   # Duplicate names will be removed

print("\nRegistered Students:")
print(students)

print("Total Unique Students:", len(students))