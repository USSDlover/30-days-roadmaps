from typing import List


def add_values_to_headers(headers: List[str], values: List[str]):
    constructed_dictionary = {}
    for index, header in enumerate(headers):
        constructed_dictionary.update({header: values[index]})
    return constructed_dictionary


def csv_to_array_of_dictionary(csv_content: List[str]):
    restructured = []
    if len(csv_content) > 0:
        headers = csv_content[0].replace('\n', '').replace(' ', '_').lower().split(',')
        csv_content.pop(0)

        for content in csv_content:
            split = content.replace('\n', '').split(',')
            content_dictionary = add_values_to_headers(headers, split)
            restructured.append(content_dictionary)

        return restructured
    else:
        print("Content is not valid")
        print(csv_content)
        return 0
