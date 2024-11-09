# List **Comprehensions:**

### what is Comprehensions?

- it is a way of writing compact  code in python.

syntax 1: Normal

```python
[expressiom for variable in iterable]
```

syntax 2: if condition

```python
[expressiom for variable in iterable if condition  ]
```

syntax 3:  if else  condition

```python
[expressiom if condition else condition for variable in iterable  ]
```

syntax 4: Nested if’s  condition

```python
[expressiom for variable in iterable if condition if condition2 ]
```

Lists are a fundamental data structure in Python, and they are widely used for tasks like storing collections of data, managing data records, and implementing various algorithms. Their flexibility and built-in methods make them a powerful tool for many programming tasks.

## What is List Comprehension?

**List comprehension is short-hand to create a new list from an existing list or iterable.**

Basically, List comprehension helps you to create a new list from an existing list in just one line.

NOTE: You can also create a completely new list using list comprehension.

Now let us create a list of squares from 1 to 10 without using list comprehension and with using list comprehension for your understanding.

**Without using list comprehension:**

```python
sq_list = []

for i in range(1,11):
    sq_list.append(i**2)

print(sq_list)
```

**Output:**

```markup
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

**With using list comprehension:**

```python
sq_list = [i**2 for i in range(1,11)]
print(sq_list)
```

**Output:**

```markup
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Creating a List of squares from 1 to 10 using list comprehension is much easier and simpler because we did it in just one line whereas we write 3-4 lines of code without using list comprehension.

## Syntax of List Comprehension

```
my_list = [expression fori initerable ifcondition ==True]
```

---

**`expression`**means what you want to **`append`** in the list.

**For Example:**



## List Comprehension with if-statement

Create a list of even numbers from existing list **`my_list = [45,12,67,8,2,6,90,13,15]`**

```python
my_list = [45,12,67,8,2,6,90,13,15]

my_list2 = [i for i in my_list if i%2 == 0]

print(my_list2)
```

**Output:**

```markup
[12, 8, 2, 6, 90]
```

### Examples for practice

Filter integer or float numbers from the list

```python
l1 = ['harsh',3,'roy','nil',1.1,25,2.1]

l2 = [i for i in l1 if (type(i) == int or type(i) == float)]

print(l2)
```

**Output:**

```markup
[3, 1.1, 25, 2.1]
```

Create a list that contains the first character of an existing list.

```python
my_fruit = ['Apple','Banana','Orange','Mango']

my_fruit2 = [i[0] for i in my_fruit]

print(my_fruit2)
```

**Output:**

```markup
['A', 'B', 'O', 'M']
```

## List Comprehension with if-else statement

Syntax of List comprehension with if-else statement


**Example:**

```python
mixed_list = ['Apple','Banana',12,15,7,2,3,'Orange','Mango']

# if type is equal to int then append square of the number
# otherwise append first character of string

mixed_list2 = [i**2 if type(i) == int else i[0] for i in mixed_list]
print(mixed_list2)
```

**Output:**

```markup
['A', 'B', 144, 225, 49, 4, 9, 'O', 'M']
```

## Nested List Comprehension

In nested List comprehension we append the whole list.

```python
l2 = [[i for i in range(3)] for j in range(3)]
print(l2)
```

**Output:**

```markup
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

1. **List Comprehensions:**
    - List comprehensions provide a concise way to create lists based on existing lists or other iterables.
    
    ```python
    
    squares = [x ** 2 for x in range(1, 6)]  # Create a list of squares
    
    ```
    
    # Using List Comprehension
    
    This approach allows us to slice the main list and the sublists **even if the sublists are not of the same length.**
    
    The general syntax for list comprehension for slicing is given in the Figure below.
    
 
    
    Here are some examples in code.
    
    ```python
    # A list within a list - the main list
    lst1 = [["Sam", 96, "Warsaw", None], ["Belinda", 78, "Israel", "GT"], ["Sally", 56, "SA", "SL"], ["Smith", 77, "Poland", "SZ"]]
    # Get the second and third elements of each sublist for the third sublist to the end
    lst2 = [sublist[1:3] for sublist in lst1[2:]]
    print("lst2: ", lst2)
    # Get the first three elements of each sublist for all sublists in the main list
    lst3 = [sublist[:3] for sublist in lst1]
    print("lst3: ", lst3)
    # Get the last two elements of the sublists for the first three sublists.
    lst4 = [sublist[-2:] for sublist in lst1[:3]]
    print("lst4: ", lst4)
    ```
    
    **Output:**
