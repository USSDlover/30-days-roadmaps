## Lists, Tuples, Dictionaries, and Sets in Python

### Table of Contents
1. [Introduction](#introduction)
2. [Lists](#lists)
3. [Tuples](#tuples)
4. [Dictionaries](#dictionaries)
5. [Sets](#sets)
6. [Challenges](#challenges)

### Introduction <a name="introduction"></a>
In Python, lists, tuples, dictionaries, and sets are fundamental data structures used to store and organize collections of data. Each of these data structures has unique characteristics and is suited for different purposes.

### Lists <a name="lists"></a>
Lists are ordered collections that can store multiple items of different data types. They are denoted by square brackets and can be modified after creation. Lists allow duplicate elements and provide indexing and slicing operations to access and manipulate the data.

Example:
```python
fruits = ['apple', 'banana', 'orange']
fruits.append('kiwi')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'kiwi']
```

### Tuples <a name="tuples"></a>
Tuples are similar to lists but are immutable, meaning they cannot be modified after creation. They are denoted by parentheses or by simply separating items with commas. Tuples are often used to represent a collection of related values that should remain unchanged.

Example:
```python
point = (3, 5)
x, y = point
print(x, y)  # Output: 3 5
```

### Dictionaries <a name="dictionaries"></a>
Dictionaries are unordered collections of key-value pairs. They are denoted by curly braces and consist of unique keys mapped to their corresponding values. Dictionaries provide fast access to values based on their keys and are useful for storing and retrieving data in a structured manner.

Example:
```python
person = {'name': 'John', 'age': 25, 'city': 'New York'}
print(person['age'])  # Output: 25
```

### Sets <a name="sets"></a>
Sets are unordered collections of unique elements. They are denoted by curly braces or by using the `set()` constructor. Sets do not allow duplicate values and offer operations such as union, intersection, and difference. They are often used for tasks like eliminating duplicates or testing membership in a collection.

Example:
```python
fruits = {'apple', 'banana', 'orange'}
fruits.add('kiwi')
print(fruits)  # Output: {'apple', 'banana', 'orange', 'kiwi'}
```

### Challenges: Movie Recommendations <a name="challenges"></a>

In this challenge, you will create a movie recommendation system using lists, tuples, dictionaries, and sets. You will have a list of movies, each represented by a dictionary with the movie title, genre, and rating. Your task is to recommend movies to users based on their preferences.

1. **Create a list of movies:**

   - Each movie should be represented as a dictionary with the following keys: 'title', 'genre', and 'rating'.
   - Include at least 10 movies in your list, covering various genres and ratings.

2. **Ask the user for their preferred genre:**

   - Prompt the user to enter a genre of their choice.
   - Store the user's input in a variable.

3. **Filter movies by genre:**

   - Iterate through the list of movies and create a new list that only includes movies matching the user's preferred genre.
   - Store the filtered movies in a new list.

4. **Ask the user for their preferred minimum rating:**

   - Prompt the user to enter a minimum rating they desire for the recommended movies.
   - Store the user's input in a variable.

5. **Filter movies by rating:**

   - Iterate through the filtered movies list and create another new list that only includes movies with a rating greater than or equal to the user's preferred minimum rating.
   - Store the final filtered movies in a new list.

6. **Display movie recommendations:**

   - If there are movies in the final filtered movies list, display the recommended movies to the user.
   - If there are no movies in the list, inform the user that no recommendations are available.

### Example Output:

```
Welcome to Movie Recommendations!

Please enter your preferred genre: Action

Please enter your preferred minimum rating (1-10): 7

Based on your preferences, we recommend the following movies:

1. Title: The Dark Knight   | Genre: Action    | Rating: 9.0
2. Title: Inception         | Genre: Action    | Rating: 8.8
3. Title: Mad Max: Fury Road| Genre: Action    | Rating: 8.1
```

### Final Code:

```python
movies = [
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Inception", "genre": "Action", "rating": 8.8},
    {"title": "Mad Max: Fury Road", "genre": "Action", "rating": 8.1},
    # Add more movies to the list
]

# Ask for user's preferences
preferred_genre = input("Please enter your preferred genre: ")
preferred_rating = float(input("Please enter your preferred minimum rating (1-10): "))

# Filter movies by genre
filtered_movies = [movie for movie in movies if movie["genre"] == preferred_genre]

# Filter movies by rating
recommended_movies = [movie for movie in filtered_movies if movie["rating"] >= preferred_rating]

# Display recommendations
print("\nBased on your preferences, we recommend the following movies:\n")
if recommended_movies:
    for i, movie in enumerate(recommended_movies, 1):
        print(f"{i}. Title: {movie['title']}   | Genre: {movie['genre']}    | Rating: {movie['rating']}")
else:
    print("No recommendations available.")
```

This challenge will help you practice working with lists, dictionaries, and filtering data based on user preferences. It will also give you hands-on experience in implementing a simple recommendation system. Feel free to expand upon the challenge by adding more features or data to make it more interesting!