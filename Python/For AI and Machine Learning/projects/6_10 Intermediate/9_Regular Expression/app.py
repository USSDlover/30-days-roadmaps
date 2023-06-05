import re


def validate_ir_phone(number):
    pattern = r"[09]{2}[1,3,2]{1}\d{8}"

    try:
        print(f"Find All: {re.findall(pattern, number)}")
        print(f"Sub it: {re.sub(pattern, 'REVERT', number)}")
        match = re.search(pattern, number)
        if match:
            print(f"Match: {match.group()}")
            return "Valid Number"
    except Exception as error:
        print(error)

    return "Invalid Number"


print(validate_ir_phone(input("Please enter your phone number: ")))
