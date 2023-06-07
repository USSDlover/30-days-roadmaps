from sales_csv import sales
from sales_operations import each_product_revenue
from utils import print_menu

parsed = sales()

command = ''

if parsed != 0:
    print_menu()

    while command != 'q':
        command = input()

        if command == 'epr':
            each_product_revenue(parsed)
            print_menu()


print("Exiting, thank you")
