from csv_parser import csv_to_array_of_dictionary


def sales():
    sales_csv = open("sales.csv", mode="r")
    parsed = csv_to_array_of_dictionary(sales_csv.readlines())
    sales_csv.close()
    return parsed

