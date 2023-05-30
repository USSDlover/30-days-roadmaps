def calc_rectangle_area(w, h):
    return w * h


# width, height = (
#     int(input('Enter width')),
#     int(input('Enter height'))
# )


def celsius_to_fahrenheit(c):
    return (c * (9 / 5)) + 32


# print(celsius_to_fahrenheit(
#     int(input('Enter Celsius: '))
# ))


def sum_even_nums_till(max_num):
    summed_num = 0
    for i in range(max_num + 1):
        if i % 2 == 0:
            summed_num += i
    return summed_num


print(sum_even_nums_till(
    int(input('Enter the max number: '))
))

