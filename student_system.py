students = {}

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    students[student_id] = {"name": name, "grade": grade}
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade']}")
    print()

def search_student():
    student_id = input("Enter ID to search: ")
    if student_id in students:
        info = students[student_id]
        print(f"Found -> Name: {info['name']}, Grade: {info['grade']}\n")
    else:
        print("Student not found.\n")

def delete_student():
    student_id = input("Enter ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student deleted.\n")
    else:
        print("Student not found.\n")

while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice\n")
