#It is a fun project
#Here i made a student record system where user can add, remove, see all student data also it can be removed if user want

# Initialize an empty dictionary to store student information
students = {}

# Define a function to add a new student


def add_student():
    # Prompt the user to enter the student's information
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    section = input("Enter student section: ")

    # Generate a user ID,  by the first letter of the student's name with their ID
    user_id = name[0].lower() + student_id

    # Add the student's information to the dictionary
    students[user_id] = {"ID": student_id, "Name": name, "Section": section}

    print("Student added successfully!")

# Define a function to print all the students


def print_students():
    print("List of students:")
    for user_id, student in students.items():
        print("User ID:", user_id)
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Section:", student["Section"])
        print("--------------")

# Define a function to search for a student


def search_student():
    # Prompt the user to enter a user ID
    user_id = input("Enter user ID: ")

    # Check if the user ID exists in the dictionary
    if user_id in students:
        # If it does, print the student's information
        print("User ID:", user_id)
        print("ID:", students[user_id]["ID"])
        print("Name:", students[user_id]["Name"])
        print("Section:", students[user_id]["Section"])
    else:
        # If it doesn't, print an error message
        print("Student not found.")

# Define a function to remove a student


def remove_student():
    # Prompt the user to enter a user ID
    user_id = input("Enter user ID: ")

    # Check if the user ID exists in the dictionary
    if user_id in students:
        # If it does, remove the student from the dictionary
        del students[user_id]
        print("Student removed successfully!")
    else:
        # If it doesn't, print an error message
        print("Student not found.")

# Define a function to display the menu options


def display_menu():
    print("Student Information System")
    print("1. Add a student")
    print("2. Print all students")
    print("3. Search for a student")
    print("4. Remove a student")
    print("5. Quit")


# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        print_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        remove_student()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


#nihal
# 220201002
# Bangladesh Army University Of Science and Tecnology        
