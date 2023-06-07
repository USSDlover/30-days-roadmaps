Here's an example of a simple library that calculates the area and perimeter of a rectangle:

1. Create a new Python module named `rectangle.py`.

2. Write the following code inside `rectangle.py`:

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)
```

3. Create another Python file named `main.py` to demonstrate how to use the library.

4. Write the following code inside `main.py`:

```python
# Importing the library module
import rectangle

# Using the library functions
length = 5
width = 3

area = rectangle.calculate_area(length, width)
perimeter = rectangle.calculate_perimeter(length, width)

print("Rectangle Area:", area)
print("Rectangle Perimeter:", perimeter)
```

5. Save both `rectangle.py` and `main.py` in the same directory.

6. Run `main.py` using the Python interpreter:

```
$ python main.py
```

Output:
```
Rectangle Area: 15
Rectangle Perimeter: 16
```

In this example, we created a library module (`rectangle.py`) that defines two functions: `calculate_area()` and `calculate_perimeter()`. These functions perform calculations based on the given length and width of a rectangle.

In the `main.py` file, we imported the `rectangle` module and used its functions to calculate the area and perimeter of a rectangle with a length of 5 and width of 3. The results were then printed to the console.

By following this approach, you can create your own libraries/modules and import them into your code to reuse the defined functionality.