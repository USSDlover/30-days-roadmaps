## Regular expressions and string manipulation

Regular expressions and string manipulation are powerful tools in Python for searching, matching, and manipulating text patterns within strings. Regular expressions, also known as regex, provide a concise and flexible way to define patterns and perform pattern matching operations on strings.

Python's built-in `re` module provides functions and methods to work with regular expressions. Here's a brief introduction to regular expressions and string manipulation in Python:

1. Pattern Matching: Regular expressions allow you to define patterns and search for specific patterns within strings. For example, you can search for email addresses, phone numbers, URLs, or any other specific pattern you define.

2. Matching Functions: Python's `re` module provides various functions to match patterns, such as `re.search()`, `re.match()`, and `re.findall()`. These functions search for a pattern in a given string and return the first match, match at the beginning of the string, or all matches, respectively.

3. Regex Patterns: Regular expressions use special characters and sequences to define patterns. For instance, `.` matches any character, `\d` matches a digit, `\w` matches a word character, and so on. You can also use quantifiers like `*`, `+`, or `{}` to specify the number of occurrences.

4. String Manipulation: In addition to pattern matching, regular expressions enable powerful string manipulation capabilities. You can use regex to replace patterns, split strings based on patterns, or extract specific parts of a string.

Here's a simple example that demonstrates the use of regular expressions in Python for pattern matching:

```python
import re

# Search for a pattern in a string
text = "Hello, my email address is example@example.com"
pattern = r'\w+@\w+\.\w+'
match = re.search(pattern, text)
if match:
    print("Found email address:", match.group())

# Replace a pattern in a string
replaced_text = re.sub(pattern, "REDACTED", text)
print("Replaced text:", replaced_text)
```

In the above example, we search for an email address pattern using a regular expression. If a match is found, we print the matched email address. Then, we use the `re.sub()` function to replace the email address with the string "REDACTED".

Regular expressions and string manipulation provide a powerful toolkit for working with text patterns in Python. They can be used for tasks like data validation, data extraction, data cleaning, and more.

By exploring and mastering regular expressions and string manipulation techniques, you can efficiently process and manipulate text data according to specific patterns and requirements.

## Common Regular Expression

Here are some common regular expression commands in Python using escape sequences:

- `\d` - Matches any digit from 0 to 9.
- `\D` - Matches any non-digit character.
- `\w` - Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore _).
- `\W` - Matches any non-alphanumeric character.
- `\s` - Matches any whitespace character (space, tab, newline, etc.).
- `\S` - Matches any non-whitespace character.
- `\b` - Matches a word boundary (position between a word and a non-word character).
- `\B` - Matches a non-word boundary.
- `\A` - Matches the start of a string.
- `\Z` - Matches the end of a string.
- `.` - Matches any character except a newline character.
- `[]` - Matches any character within the brackets. For example, `[aeiou]` matches any lowercase vowel.
- `[^]` - Matches any character not within the brackets. For example, `[^aeiou]` matches any character that is not a lowercase vowel.
- `*` - Matches zero or more occurrences of the preceding pattern.
- `+` - Matches one or more occurrences of the preceding pattern.
- `?` - Matches zero or one occurrence of the preceding pattern.
- `{n}` - Matches exactly n occurrences of the preceding pattern.
- `{n,}` - Matches n or more occurrences of the preceding pattern.
- `{n,m}` - Matches between n and m occurrences of the preceding pattern.

These are just a few examples of regular expression commands in Python. Regular expressions are a powerful tool for pattern matching and manipulating strings. You can use the `re` module in Python to work with regular expressions. It provides functions such as `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and string manipulation operations. Make sure to consult the [Python documentation](https://docs.python.org/3/library/re.html) for the `re` module for more details and additional functionality.