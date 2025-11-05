## Higher order functions()

Function which takes other functions as arguments is called Higher order functions

Three built in higher order functions:

1. filter()
2. map()
3. reduce()

### filter()

filter() is used to filter out  the elements of iterable based on a condition and it takes 2 arguments which is function name and iterable

syntax:

```python
filter(function_name,iterable)
```

- function_name :- function that tests every element of iterable
- iterable:- sequence which needs to be filtered

```python
numbers=[67,89,91,34,55,45,46,78]  # iterable elements of list

def filter_even(val): # function
	if val%2==0:
		return True
filtered_object=filter(filter_even,numbers)

print(filtered_object)
print( type(filtered_object))
print(list(filtered_object))
```

```python
<filter object at 0x000001EA6A3B45E0>
<class 'filter'>
[34, 46, 78]
```

**imp:**

**filter() returns filtered objects**

**filtered objects are temporary objects**

**in filter() only once we can consume(use) the items .**

**and again we try to print them then it returns empty**

**if we want to print filtered object multiple times we need to  type caste that to list**

```python
filtered_object=list(filter(filter_even,numberes))
```

```python
numbers=[67,89,91,34,55,45,46,78]

def filter_even(val):
	if val%2==0:
		return True
filtered_object=filter(filter_even,numbers)
print(filtered_object)
print( type(filtered_object))

# here we are using filter object
print(list(filtered_object))

# again we are using filter object but here returns empty list
print(list(filtered_object))

```

```python
<filter object at 0x000001F5F3CD45E0>
<class 'filter'>
[34, 46, 78]
[]
```

### for loop

```python

numbers=[67,89,91,34,55,45,46,78]

def filter_even(val):
	if val%2==0:
		return True
filtered_object=filter(filter_even,numbers)
print(filtered_object)
print( type(filtered_object))
for ele in filtered_object:
	print(ele)
```

```python
<filter object at 0x00000293D60145E0>
<class 'filter'>
34
46
78
```

```python
numbers=[67,89,91,34,55,45,46,78]

def filter_even(val):
	if val%2==0:
		return True
filtered_object=filter(filter_even,numbers)
print(filtered_object)
print( type(filtered_object))

# here retuns the items from iterable
for ele in filtered_object:
	print(ele)

# here again we try to iterate them retun nothing
for el in filtered_object:
	print(el)
```

```python
<filter object at 0x00000221A16045E0>
<class 'filter'>
34
46
78
```

```python
values=[False,True,True,0,45,None,False,1]
print(list(filter(None,values)))

```

```python
[True, True, 45, 1]
```

## filter() using lambada function

syntax:

```python
filter(lambda expression,iterables)
```

```python
numbers=[67,86,45,66,54,31,98,63]
filtered_object=filter(lambda x:x%2==0,numbers)
print(list(filtered_object))
```

```python
[86, 66, 54, 98]
```

example:

Write a python program for filtering products according to budget.

```python
laptops={'Asus':75000,'Hp':60000,'Dell':45000,'lenovo':35000,'mac':120000}
budget=float(input('Enter your budget: '))
def filter_lappy(ele):
	if laptops[ele]<=budget:
		return True
	else:
		return False
filtered_object=filter(filter_lappy,laptops)
print(list(filtered_object))
```

```python
Enter your budget: 45000
['Dell', 'lenovo']
```

# map() function

map() function is a built-in higher order function it apply a specified function on each element of the iterable and perhaps change element.

the **`map()`** function is a built-in function that applies a specified function to all items in an input iterable (e.g., a list, tuple) and returns an iterator that produces the results. The  function has the following syntax:

syntax:

```python
map(function_name,iterable)
```

- **`function_name`**: The function to apply to each item in the iterable.
- **`iterable`**: The iterable (e.g., a list, tuple) whose items will be processed by the function.

Here's a simple example:

```python

# Define a function to square a number
def square(x):
    return x ** 2

# Use map to apply the function to a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

# Convert the iterator to a list for printing
result_list = list(squared_numbers)

print(result_list)  # Output: [1, 4, 9, 16, 25]

```

In this example, the **`square`** function is applied to each element in the **`numbers`** list using **`map()`**. The result is an iterator that produces squared numbers.

### **Using Lambda Function with `map()`:**

**`map()`** is often used in conjunction with lambda functions for short, one-time operations. Here's an example:

```python

# Use map with a lambda function to double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)

# Convert the iterator to a list for printing
result_list = list(doubled_numbers)

print(result_list)  # Output: [2, 4, 6, 8, 10]

```

In this example, a lambda function is used to double each element in the **`numbers`** list.

### **Mapping Multiple Iterables:**

You can also use **`map()`** with multiple iterables. The provided function should take as many arguments as there are iterables.

```python

# Use map with a function and two iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = map(lambda x, y: x + y, list1, list2)

# Convert the iterator to a list for printing
result_list = list(sums)

print(result_list)  # Output: [5, 7, 9]

```

In this example, the lambda function takes elements from **`list1`** and **`list2`** and calculates their sum.

Note: In Python 3, **`map()`** returns an iterator, so you often need to convert it to a list or another iterable type to see the results.

# reduce()

The **`reduce()`** function is another built-in function in Python that is part of the **`functools`** module. It is used to apply a specified function in a cumulative way to the items of an iterable, reducing the iterable to a single accumulated result. The **`reduce()`** function has the following syntax:

```python

functools.reduce(function, iterable[, initializer])

```

- **`function`**: The function to apply cumulatively to the items of the iterable. It should take two arguments and return a single value.
- **`iterable`**: The iterable (e.g., a list, tuple) whose items will be processed by the function.
- **`initializer`** (optional): If provided, it is placed before the items of the iterable in the calculation and serves as a default when the iterable is empty.

Here's a simple example using **`reduce()`** to find the product of elements in a list:

```python

from functools import reduce

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Use reduce to find the product of numbers in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)

print(product)  # Output: 120

```

In this example, the **`multiply`** function is applied cumulatively to the elements of the **`numbers`** list, resulting in the product.

### **Using `reduce()` with Lambda Function:**

**`reduce()`** is often used in conjunction with lambda functions for short, one-time operations. Here's an example finding the maximum element in a list:

```python

from functools import reduce

# Use reduce with a lambda function to find the maximum element in a list
numbers = [3, 7, 2, 8, 5]
max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(max_number)  # Output: 8

```

In this example, the lambda function compares two elements and returns the larger one, and **`reduce()`** applies it cumulatively to find the maximum element.

### **Using `reduce()` with Initializer:**

You can also provide an optional initializer argument to **`reduce()`**. This value is used as the starting point for the cumulative calculation.

```python

from functools import reduce

# Use reduce with an initializer to find the sum of numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers, 0)

print(sum_result)  # Output: 15

```

In this example, the **`reduce()`** function starts with an initializer of **`0`** and calculates the sum of the numbers in the list.

**`reduce()`** is a powerful tool for cumulative operations on iterables, and it's particularly useful when you need to perform a rolling or accumulating calculation on a sequence of values.
