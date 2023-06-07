## Introduction to NumPy (arrays, mathematical operations, indexing)

NumPy is a fundamental library in Python for numerical computing. It provides support for efficient array operations and mathematical computations. This introduction will cover the basics of working with NumPy arrays, performing mathematical operations, and indexing elements within arrays.

### Example
Let's consider an example of creating a NumPy array and performing mathematical operations on it. We want to create an array of numbers representing the ages of a group of people and find the average age.

```python
import numpy as np

# Creating a NumPy array
ages = np.array([25, 30, 28, 32, 27])

# Calculating the average age
average_age = np.mean(ages)

print("Average age:", average_age)
```

### Challenge
To solidify your understanding, here's a challenge for you:

Given a NumPy array `prices` representing the prices of different products, write code to find the maximum and minimum prices, and calculate the range (difference between the maximum and minimum) of the prices.

```python
import numpy as np

# Example array of prices
prices = np.array([10.99, 5.99, 8.75, 12.50, 6.25])

# Find maximum price
max_price = np.max(prices)

# Find minimum price
min_price = np.min(prices)

# Calculate range of prices
price_range = max_price - min_price

print("Maximum price:", max_price)
print("Minimum price:", min_price)
print("Price range:", price_range)
```

This challenge will help you practice using NumPy functions to extract valuable insights from arrays. Feel free to experiment with different arrays and explore other NumPy functions for further learning.

Good luck with your exploration of NumPy!