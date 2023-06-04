class CustomException(Exception):
    pass


def divide_numbers(num1, num2):
    if num2 == 0:
        raise CustomException("Error: Division by zero is not allowed.")
    else:
        return num1 / num2
