# Manuplation of strings

String manipulation refers to the process of modifying or manipulating strings in various ways, such as extracting substrings, replacing characters, converting case, concatenating, splitting, and more. Here are some common string manipulation operations in Python.

## 1. `Concatenation`:

- Combining multiple strings together using the ' + '  operator or the str.join() method.

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Concatenation using the + operator
print(result)

# Output: Hello World
```

- join() method.

```python
# concatenation using  .join()

str1 = "Hello"
str2 = "World"
result = " ".join([str1, str2])  # Concatenation using str.join()
print(result) 

# Output: Hello World

```

```
# concatenation using  .join()

result=" ".join(["Hello"+" "+ "World"])
print(result)

# Output: Hello World
```

## 2. `Substring Extraction`:

 Extracting a portion of a string based on indices using slicing.

```
string = "Hello, World!"
substring = string[7:12]  # Extracting the substring "World"
print(substring)

# Output: World

```

## `3.String Length`:

- Getting the length of a string using the len() function.

```python
string = "Hello"
length = len(string)  # Length of the string
print(length)
# Output: 5

```

## `4.Changing Case`:

- Converting the case of a string using the str.lower() and str.upper() methods.

```python
string = "Hello, World!"
lowercase = string.lower()  # Converting to lowercase
uppercase = string.upper()  # Converting to uppercase
print(lowercase)
print(uppercase)

# Output: hello, world!
# Output: HELLO, WORLD!

```

## `5.String Replacement`:

- Replacing substrings within a string using the str.replace() method.

```python
# string replacement with replace()

string = "Hello, World!"
new_string = string.replace("World", "Python")  # Replacing "World" with "Python"
print(new_string)

# Output: Hello, Python!

```

## `6.Splitting and Joining`:

Splitting a string into a list of substrings using str.split() and joining a list of strings into a single string using str.join().

```python
# Splitting and Joining

string = "Hello, World!"
words = string.split(", ")  # Splitting into words
print(words)


joined_string = "-".join(words)  # Joining words with a hyphen
print(joined_string)

# Output: ['Hello', 'World!'] 
# Output: Hello-World!

```

## `7. Stripping Whitespace`:

- Stripping whitespace from the beginning and end of a string using the str.strip() method.
- Stripping whitespace from a string involves removing any leading or trailing spaces, tabs, or newline characters. Python provides several methods to accomplish this:

## 1. `str.strip()`:

- Removes leading and trailing whitespace from a string.

```python
# Removing whitespace using strip()

string = "   Hello, World!   "
stripped_string = string.strip()
print(stripped_string) 

 # Output: Hello, World!

```

2. `str.lstrip() `:

- Removes leading(starting) whitespace from a string.

```python
#
string = "   Hello, World!   "
stripped_string = string.lstrip()
print(stripped_string) 
 # Output: Hello, World!   

```

## `3. str.rstrip()`:

- Removes trailing (ending) whitespace from a string.

```python
string = "   Hello, World!   "
stripped_string = string.rstrip()
print(stripped_string) 

 # Output: "   Hello, World!"

```

- These methods return a new string with the whitespace stripped. The original string remains unchanged.
- It's important to note that these methods only remove leading and trailing whitespace. If you want to remove all whitespace from a string, you can use the `str.replace()` method or a combination of `str.split()` and `str.join()`.

For Example:

```python
# removing white spaces using replace()

string = "   Hello, World!   "
stripped_string = string.replace(" ", "")
print(stripped_string)  

# Output: Hello,World!

```

# F-strings

- f-strings, also known as formatted string literals, provide a concise and convenient way to embed expressions within string literals in Python. They were introduced in Python 3.6 and provide a more readable and efficient way of string interpolation.
- To create an f-string, you can prefix the string literal with the letter "f" or "F" and enclose the expressions to be evaluated within curly braces {}. Here's an example:

```python
name = "Alice"
age = 25

# Example 1: Simple f-string
greeting = f"Hello, {name}!"
print(greeting) 

 # Output: "Hello, Alice!"

# Example 2: Expressions within f-string
info = f"Name: {name}, Age: {age}, Birth Year: {2023 - age}"
print(info) 

 # Output: "Name: Alice, Age: 25, Birth Year: 1998"

```

## Assignment

- 1. Write a program to print the no of characters in the name entered by user using len() function.
