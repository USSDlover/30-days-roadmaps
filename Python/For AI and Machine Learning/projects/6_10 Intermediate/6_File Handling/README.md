## Introduction to File Handling in Python

File handling in Python refers to the process of reading and writing data to and from files. It allows you to work with different types of files, such as text files, CSV files, JSON files, and more. Python provides built-in functions and methods to interact with files, making it easy to perform operations like opening, reading, writing, and closing files.

### Reading Data from a File

To read data from a file in Python, you can use the `open()` function to open the file and then use the `read()` or `readlines()` methods to access the file's contents.

```python
# Opening a file in read mode
file = open('data.txt', 'r')

# Reading the entire file content
content = file.read()
print(content)

# Alternatively, reading line by line
lines = file.readlines()
for line in lines:
    print(line)

# Closing the file
file.close()
```

### Writing Data to a File

To write data to a file in Python, you need to open the file in write mode ('w' or 'a' for append) using the `open()` function. Then, you can use the `write()` method to write data to the file.

```python
# Opening a file in write mode
file = open('output.txt', 'w')

# Writing content to the file
file.write("Hello, world!\n")
file.write("This is a sample text.")

# Closing the file
file.close()
```

### Challenge: Student Grade Management

Create a program that manages student grades by reading and writing data to a file. The program should have the following functionalities:

1. Allow the user to enter student names and their corresponding grades.
2. Write the student data to a file.
3. Provide an option to read and display the student data from the file.
4. Calculate the average grade for each student and display it.

You can structure the data in the file using a suitable format, such as CSV or JSON. Implementing this challenge will give you hands-on experience with file handling, data input/output, and basic data manipulation in Python.

Remember to handle any potential errors or exceptions that may occur during file operations.