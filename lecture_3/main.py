"""
Student Grade Analyzer
----------------------
A console-based application for managing students and their grades.

Features:
1. Add new students
2. Add grades to a student
3. Generate a full report
4. Identify the top performer
5. Exit the program
"""


def add_student(students, name):
    """Add a new student to the list if not already present.

    Args:
        students (list): List of dictionaries representing students.
        name (str): Name of the student to add.

    Returns:
        bool: True if the student was added, False if already exists.
    """
    if any(s['name'] == name for s in students):
        return False
    students.append({'name': name, 'grades': []})
    return True


def find_student(students, name):
    """Find a student by name in the list.

    Args:
        students (list): List of dictionaries representing students.
        name (str): Name of the student to find.

    Returns:
        dict or None: Student dictionary if found, otherwise None.
    """
    for student in students:
        if student['name'] == name:
            return student
    return None


def add_grades_interactive(student):
    """Interactively read and store valid grades for a student.

    Prompts user for input until 'done' is entered.
    Only integers in the range [0, 100] are accepted and stored.

    Args:
        student (dict): Student dictionary with a 'grades' key (list).

    Returns:
        None
    """
    while True:
        print("Enter a grade (or 'done' to finish): ", end='')
        input_grade = input()
        if input_grade.lower() == 'done':
            break
        try:
            grade = int(input_grade)
            if 0 <= grade <= 100:
                student['grades'].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid number. Please enter a number.")


def calculate_average(grades):
    """Calculate the arithmetic mean of a list of grades.

    Args:
        grades (list of int): List of numeric grades.

    Returns:
        float or None: Average grade if list is non-empty, otherwise None.
    """
    return sum(grades) / len(grades) if grades else None


def generate_report(students):
    """Generate a formatted textual report for all students.

    Students are sorted by average grade in descending order.
    Students with no grades (N/A) appear at the end.

    Args:
        students (list): List of student dictionaries.

    Returns:
        list of str: Lines of the report ready for printing.
    """
    if not students:
        return ["No students to report on."]

    with_grades = []
    without_grades = []
    averages = []

    for student in students:
        if student['grades']:
            avg = calculate_average(student['grades'])
            with_grades.append((student, avg))
            averages.append(avg)
        else:
            without_grades.append(student)

    with_grades.sort(key=lambda x: x[1], reverse=True)

    lines = []
    for student, avg in with_grades:
        lines.append(f"{student['name']}'s average grade is {avg:.1f}.")
    for student in without_grades:
        lines.append(f"{student['name']}'s average grade is N/A.")

    if averages:
        lines.extend([
            "-" * 20,
            f"Max Average: {max(averages):.1f}",
            f"Min Average: {min(averages):.1f}",
            f"Overall Average: {sum(averages) / len(averages):.1f}"
        ])

    return lines


def find_top_student(students):
    """Identify the student with the highest average grade.

    Only students with at least one grade are considered.

    Args:
        students (list): List of student dictionaries.

    Returns:
        tuple or None: (name: str, average: float) of top student,
                       or None if no student has grades.
    """
    valid = [student for student in students if student['grades']]
    if not valid:
        return None
    best = max(valid, key=lambda s: calculate_average(s['grades']))
    avg = calculate_average(best['grades'])
    return best['name'], avg


def display_menu():
    """Display the main interactive menu options to the user.
    Returns:
        None
    """
    print("\n--- Student Grade Analyzer ---")
    print("1. Add a new student")
    print("2. Add grades for a student")
    print("3. Generate a full report")
    print("4. Find the top student")
    print("5. Exit program")


def main():
    """Run the main application loop.

    Manages user interaction, dispatches to appropriate functions,
    and handles basic input validation for menu choices.

    Returns:
        None
    """
    students = []

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            raw_name = input("Enter student name: ").strip()
            if not raw_name:
                print("Name cannot be empty.")
                continue
            name = raw_name.title()
            if add_student(students, name):
                print(f"Student '{name}' added.")
            else:
                print(f"Student '{name}' already exists.")

        elif choice == 2:
            raw_name = input("Enter student name: ").strip()
            if not raw_name:
                print("Name cannot be empty.")
                continue
            name = raw_name.title()
            student = find_student(students, name)
            if student:
                add_grades_interactive(student)
            else:
                print(f"Student '{name}' not found.")

        elif choice == 3:
            print("--- Student Report ---")
            for line in generate_report(students):
                print(line)

        elif choice == 4:
            top = find_top_student(students)
            if top:
                name, avg = top
                print(f"The student with the highest average is {name} with a grade of {avg:.1f}.")
            elif not students:
                print("No students have been added yet.")
            else:
                print("No students have grades yet.")

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
