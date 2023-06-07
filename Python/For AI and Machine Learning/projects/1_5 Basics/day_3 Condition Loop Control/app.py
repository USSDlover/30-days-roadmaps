def user_eligible(age):
    if age >= 18:
        print("You are eligible for voting")
    else:
        print("Unfortunately you are not eligible")


# user_eligible(int(input("Please Enter your age: ")))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            print("Leap Year")
        elif year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            elif year % 400 != 0:
                print("Not Leap Year")
    else:
        print(f"{year} is not a leap year")


# is_leap_year(int(input("Enter the year: ")))


def ask_and_sum():
    user_input = 0
    summed = 0
    shall_continue = True

    while shall_continue:
        user_input = int(input("Enter the number: "))

        if user_input < 0:
            shall_continue = False
            break

        summed += user_input
        print(f"Sum: {summed}")


# ask_and_sum()
