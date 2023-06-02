from typing import List, Dict


def new_student():
    name = input("Student Name: ")
    age = int(input("Student Age: "))
    grade = int(input("Student Grade: "))

    students_csv = open("students.csv", "a")
    students_csv.write(f"{name.capitalize()}, {age}, {grade}\n")
    students_csv.close()
    print(f"{name} Added")


def edit_student(parsed_students: List[Dict]):
    student, index = find_student(parsed_students)
    if student:
        print(student, index)

        command = 'e'
        print('e - Continue Editing | s - Save Changes | d - Discard Changes')

    def edit_name():
        updated_name = input("Enter new name: ")
        student["name"] = updated_name


def find_student(parsed_students: List[Dict]):
    name = input("Student Name: ").lower()
    student = {"name": name}
    student_index = 0
    for index, std in enumerate(parsed_students):
        split_full_name = std["name"].split(" ")
        if len(split_full_name) > 1:
            if split_full_name[0].lower() == name:
                student = std
                student_index = index
            elif split_full_name[1].lower() == name:
                student = std
                student_index = index
        elif std["name"] == name:
            student = std
            student_index = index

    try:
        if student["age"]:
            return student, student_index
    except KeyError:
        print(f"Where not able to find the user with name: {student['name']}")
