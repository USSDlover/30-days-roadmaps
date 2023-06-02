from csv_parser import csv_to_dic


def students():
    students_csv = open("students.csv", mode="r")
    parsed = csv_to_dic(students_csv.readlines())
    students_csv.close()
    return parsed

