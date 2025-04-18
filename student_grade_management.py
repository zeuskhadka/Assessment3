import random

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# This is the function to check if the student passed or failed

def check_pass_fail(average):
    if average >= 50:
        return "Passed"
    else:
        return "Failed"

# Main function helps to manage the process

def main():
    students = []  # I am creating list to store student data
    #I am using the infinite loop over here
    while True:

        print("\n--- Student Grade Adventure ---")
        print("1. Add Student Data")
        print("2. View All Students Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Step 1: Get student name, roll number, and grades
            name = input("Enter student's name: ")
            roll_no = input("Enter student's roll number: ")
            grades = []

            # Input grades for 3 subjects
            for i in range(3):
                grade = float(input(f"Enter grade for subject {i + 1}: "))
                grades.append(grade)

            # I am processing student data
            average = calculate_average(grades)
            result = check_pass_fail(average)

            # I am Storing the student's information
            students.append((name, roll_no, grades, average, result))
            print(f"Student {name} added successfully!")

        elif choice == '2':
            #  Displaying student data
            print("\n--- All Students Data ---")
            for student in students:
                name, roll_no, grades, average, result = student
                print(
                    f"Name: {name}, Roll No: {roll_no}, Grades: {grades}, Average: {average}, Result: {result}")

        elif choice == '3':
            print("Goodbye! 👋")
            break  # Exit the program

        else:
            print("Invalid choice, please try again.")


# Start the program
main()
