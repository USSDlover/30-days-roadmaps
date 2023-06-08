import numpy as np
from typing import List


def get_max_by_attribute(array, attribute):
    values = np.array([dictionary[attribute] for dictionary in array])
    max_index = np.argmax(values)
    return array[max_index]


def merge_dicts(array: List[dict], attribute):
    # Get values of the attribute in dict
    values = np.array([dictionary[attribute] for dictionary in array])
    # Remove duplicates
    unique_values = np.unique(values)

    merged_array: List[dict] = []
    # Use unique values to find dictionaries in array with the unique value
    for value in unique_values:
        merged_dict = {}
        # Go through dictionaries inside the array argument to find the value same as this one
        for dictionary in array:
            # dict.name("john") == "john"
            if dictionary[attribute] == value:
                # To add the keys to merged_dict one by one
                for dict_key in dictionary.keys():
                    if (dict_key == "quantity_sold") | (dict_key == "revenue"):
                        try:
                            if dict_key in merged_dict:
                                merged_dict.update({dict_key: int(dictionary.get(dict_key)) + int(merged_dict.get(dict_key))})
                            else:
                                merged_dict.update({dict_key: dictionary.get(dict_key)})
                        except Exception as e:
                            print(f"Error on adding QS: {e}")
                    else:
                        merged_dict.update({f"{dict_key}": dictionary.get(dict_key)})
        merged_array.append(merged_dict)

    return merged_array


def each_product_revenue(sales: List[dict]):
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
