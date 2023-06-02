from students_csv import students
from student_operations import new_student, edit_student, find_student
from utils import print_menu

parsed = students()

command = ''

if parsed != 0:
    print_menu()

    while command != 'q':
        command = input()

        if command == 'a':
            new_student()
            parsed = students()
            print_menu()

        if command == 'e':
            edit_student(parsed)
            parsed = students()
            print_menu()

        if command == 'l':
            print(parsed)
            print_menu()

        if command == 'f':
            print(find_student(parsed))
            print_menu()


print("Exiting, thank you")
