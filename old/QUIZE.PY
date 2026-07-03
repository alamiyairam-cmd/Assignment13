# ==========================
# QUIZ AND EXAMINATION SYSTEM
# ==========================

# List of tuples to store questions
questions = [
    ("Python is a ?", "Programming Language", "Database", "Browser", "Game", "A"),
    ("Which data type is immutable?", "List", "Dictionary", "Tuple", "Set", "C"),
    ("Keyword to define a function?", "fun", "define", "def", "function", "C"),
    ("Which loop repeats until condition is false?", "for", "while", "if", "else", "B"),
    ("Which symbol is used for comments?", "#", "//", "/*", "$", "A")
]

# Function to calculate grade
def calculate_grade(percent):
    if percent >= 90:
        return "O"
    elif percent >= 80:
        return "A+"
    elif percent >= 70:
        return "A"
    elif percent >= 60:
        return "B+"
    elif percent >= 50:
        return "B"
    else:
        return "F"

# Function to conduct quiz
def evaluate_quiz():

    score = 0

    # List to store wrong answers
    wrong_answers = []

    # Loop through questions
    for q in questions:

        print("\n", q[0])
        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])

        # String operation using strip() and upper()
        answer = input("Enter Answer (A/B/C/D): ").strip().upper()

        # Input validation
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid Choice!")
            answer = input("Enter Again: ").strip().upper()

        # Check answer
        if answer == q[5]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            wrong_answers.append((q[0], q[5]))

    # Arithmetic operation
    percent = (score / len(questions)) * 100

    grade = calculate_grade(percent)

    # Display result
    print("\n===== RESULT =====")
    print("Score :", score, "/", len(questions))
    print("Percentage :", percent)
    print("Grade :", grade)

    # Pass or Fail using conditional statement
    if percent >= 50:
        print("Result : PASS")
    else:
        print("Result : FAIL")

    # Show wrong answers
    if len(wrong_answers) > 0:
        print("\nWrong Answers:")
        for item in wrong_answers:
            print("Question :", item[0])
            print("Correct Answer :", item[1])

# Main Program
try:
    # Input from user
    name = input("Enter Student Name: ").strip().title()
    roll = int(input("Enter Roll Number: "))

    print("\nWelcome", name)

    # Call function
    evaluate_quiz()

except ValueError:
    # Exception handling
    print("Invalid Input!")