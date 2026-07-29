# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================

def add_student(students):
    """Add a new student record to the students list."""
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Student ID must be a number.")
        return

    try:
        count = int(input("How many scores? "))
    except ValueError:
        print("Number of scores must be a valid integer.")
        return

    if count < 0:
        print("Number of scores cannot be negative.")
        return

    scores = []
    for i in range(1, count + 1):
        try:
            score = float(input(f"Enter score {i}: "))
        except ValueError:
            print("Scores must be numeric.")
            return
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }
    students.append(student)
    print(f'Student "{name}" added successfully.')


def display_students(students):
    """Display all student records in a formatted table."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15} {'ID':<10} {'Scores':<20} {'Average'}")
    print("-" * 50)

    for student in students:
        scores_text = ", ".join(str(score) for score in student["scores"])
        average = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
        print(f"{student['name']:<15} {student['id']:<10} {scores_text:<20} {average:.2f}")

    print("-" * 50)


def calculate_average(students):
    """Calculate and display the average score for a specific student ID."""
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Student ID must be a number.")
        return

    for student in students:
        if student["id"] == student_id:
            average = sum(student["scores"]) / len(student["scores"]) if student["scores"] else 0
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Student ID not found.")


def main():
    students = []

    while True:
        print("\n===============================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("===============================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()

