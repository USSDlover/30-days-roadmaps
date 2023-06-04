from CustomException import CustomException, divide_numbers

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = divide_numbers(num1, num2)
    print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except CustomException:
    print(CustomException)
