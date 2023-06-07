import numpy as np
from typing import List


def merge_dicts(array: List[dict], attribute):
    # Get values of the attribute in dict
    keys = np.array([dictionary[attribute] for dictionary in array])
    print(f"Keys: {keys}")
    # Remove duplicates
    unique_keys = np.unique(keys)
    print(f"Unique Keys: {unique_keys}")

    merged_array: List[dict] = []
    for key in unique_keys:
        merged_dict = {}
        for dictionary in array:
            if dictionary[attribute] == key:
                for dict_key in dictionary.keys():
                    if dict_key == "quantity_sold":
                        dictionary.update({"quantity_sold": int(dictionary.get(dict_key)) + int(merged_dict.get(dict_key))})

                    if dict_key == "revenue":
                        dictionary.update({"revenue": int(dictionary.get(dict_key)) + int(merged_dict.get(dict_key))})

                    merged_dict.update(dictionary)
        merged_array.append(merged_dict)

    return merged_array


def each_product_revenue(sales: List[dict]):
    # print("Calculate each product total revenue")
    print(f"Received this sales: {sales[0].keys()}")
    try:
        merged_sales = merge_dicts(sales, "product")
        print(f"Merged sales: {merged_sales}")
    except Exception as error:
        print(f"Error on generating each product revenue: {error}")


def top_selling_product():
    print("Determine the top-selling product based on the total quantity sold")


def region_average_revenue():
    print("Calculate the average revenue generated per region")


def highest_revenue_region():
    print("Identify the region with the highest total revenue")
