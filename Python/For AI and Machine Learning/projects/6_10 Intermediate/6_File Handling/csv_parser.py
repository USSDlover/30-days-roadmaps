from typing import List


def csv_to_dic(csv_content: List[str]):
    restructured = []
    if len(csv_content) > 0:
        headers = csv_content[0].replace('\n', '').lower().split(',')
        csv_content.pop(0)

        for content in csv_content:
            split = content.replace('\n', '').split(',')
            dic_content = {
                headers[0]: split[0],
                headers[1]: split[1],
                headers[2]: split[2]
            }
            restructured.append(dic_content)

        return restructured
    else:
        print("Content is not valid")
        print(csv_content)
        return 0
