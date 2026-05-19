def add_student(students):
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    age = input("Enter student age: ").strip()
    grade = input("Enter student grade: ").strip()
    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
    })
    print("Student added")


def view_students(students):
    if not students:
        print("No students found")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def find_student(students, keyword):
    keyword = keyword.lower()
    for s in students:
        if s["id"].lower() == keyword or s["name"].lower() == keyword:
            return s
    return None


def update_student(students):
    keyword = input("Enter ID or name to update: ").strip()
    student = find_student(students, keyword)
    if not student:
        print("Student not found")
        return

    name = input("Enter new name (leave blank to keep): ").strip()
    age = input("Enter new age (leave blank to keep): ").strip()
    grade = input("Enter new grade (leave blank to keep): ").strip()

    if name:
        student["name"] = name
    if age:
        student["age"] = age
    if grade:
        student["grade"] = grade

    print("Student updated")


def delete_student(students):
    keyword = input("Enter ID or name to delete: ").strip()
    student = find_student(students, keyword)
    if not student:
        print("Student not found")
        return
    students.remove(student)
    print("Student deleted")


def menu():
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by ID/name")
    print("4. Update student record")
    print("5. Delete student record")
    print("6. Exit")


def main():
    students = []
    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            keyword = input("Enter ID or name to search: ").strip()
            student = find_student(students, keyword)
            if student:
                print(f"Found: ID {student['id']}, Name {student['name']}, Age {student['age']}, Grade {student['grade']}")
            else:
                print("Student not found")
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
