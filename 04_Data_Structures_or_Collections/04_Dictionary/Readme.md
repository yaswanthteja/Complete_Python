## What is Dictionary in python?

A dictionary is a built-in data structure in python and it is used to store an unordered collection of items in the form of a ***key: value*** pair.

**OR** you can say, that dictionary is an unordered collection of data in *****a **key: value*** pair.

# Dictionary

They are also known as mapping type, they map keys to the values.

## What data types you can use for keys in Python dictionary?

Any data type which is immutable can be used as a key. To understand this behavior we would
need to understand how dictionary works behind the scene, which is too
advanced for this course.

For now just remember that immutable data types such as **string, int, float, boolean, tuples,** etc, can be used
as keys.

```python
pizza = {
        10: "small",
        8.99: "price",
        ("cheese", "olives"): "toppings",
        True: "available",
    }

print(pizza[10]) # prints => "small"
print(pizza[8.99]) # prints => "price"
print(pizza[("cheese", "olives")]) # prints => "toppings"
print(pizza[True]) # prints => "available"
```

`pizza` is also a perfectly valid dictionary, but does not have practical usability.


key of dictionary is always unique and value may or may not be unique.

## Why we use dictionary?

Due to the limitations of a list, list is not sufficient to represent real-life data.

## Create a dictionary

there are two ways to create a dictionary in python.

1. using curly brackets ‘**{ }**‘
2. using **`dict()`** function

### Create a dictionary using curly brackets.

To create a dictionary in Python write comma-separated data in the form of a **`key: value`** pair inside the curly bracket.

**Example:**

```python
name = {'name':'saurabh','age':19,'collage':'unknown'}
print(name)
```

**Output:**

```markup
{'name': 'saurabh', 'age': 19, 'collage': 'unknown'}
```

### Create a dictionary using function.

You can also use the **`dict()`** function to create a dictionary in Python. let’s see it with the help of an example.

```python
user1 = dict(name = "ibrahim",age = 20,collage = "unknown")
print(user1)
```

**Output:**

```markup
{'name': 'ibrahim', 'age': 20, 'collage': 'unknown'}
```

When you create a dictionary using the **`dict()`** function, *write **key** **= value*** (int, list, float, tuple, etc..).

## Access data from the dictionary

With the help of keys, you can access the data of a dictionary because a dictionary is an unordered collection of data and there is no indexing.

write a square bracket after the name of the dictionary and inside a square bracket write your key to get the value of a specified key. If a key is not present in your dictionary it will give an error.

```python
user1 = dict(name = "yash",age = 20,collage = "unknown")
print(user1['name']) # yash
print(user1['gender']) # error
```

**Output:**

```markup
yash
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(user1['gender'])
KeyError: 'gender'
```

### get() method

You can also use the **`.get()`** method to access data from the dictionary and it will not give an error if the key is not present in the dictionary.

**Example:**

```python
user1 = dict(name = "yash",age = 20,collage = "unknown")
print(user1.get('age')) # 20
print(user1.get('gender')) # None
```

**Output:**

```markup
20
None
```

By default, the **`.get()`** method returns **`None`** if the key is not found, but you can also print custom text if you want. Just add a comma after specifying the key within the **`.get()`** method and pass your custom text.

```python
user1 = dict(name = "yash",age = 20,collage = "unknown")
print(user1.get('age')) # 20
print(user1.get('gender','Not Found'))
```

**Output:**

```markup
20
Not Found
```

## Which type of data a dictionary can store?

You can store anything (number, string, list, dictionary, tuple, etc.) inside a dictionary.

**Example:**

```python
user_info = {
    'name': 'ram',
    'age': 24,
    'fav_movie': ['coco','dolittle'],
    'fav_tune': ['awakening','fairy tale']
}
print(user_info)
print(user_info['fav_movie'])
```

**Output:**

```markup
{'name': 'ram', 'age': 24, 'fav_movie': ['coco', 'dolittle'], 'fav_tune': ['awakening', 'fairy tale']}
['coco', 'dolittle']
```

## Add data in the dictionary

Let’s understand how to add data in the dictionary with the help of an example.

```python
my_info = {} #create empty dictionary
print(my_info)
my_info['name'] = 'harshit'   #add data to dictionary
my_info['age'] = 25

print(my_info) #data is added in dictionary
```

**Output:**

```markup
{}
{'name': 'harshit', 'age': 25}
```

## Delete data from a dictionary

There are mainly two methods used to delete data from a dictionary and they are.

1. pop() method
2. popitem() method

### pop() Method

A pop() method is used to remove the value of a specified key.

*syntex –> dictionary_name.pop(key_name)*

**Example:**

```python
number1 = {
    "game":"BGMI",
    "singer":"arjit singh",
    "cricketer":"virat kohli"
}
print("before pop")
print(number1)

number1.pop('singer')

print("after pop")
print(number1)
```

```markup
before pop
{'game': 'BGMI', 'singer': 'arjit singh', 'cricketer': 'virat kohli'}
after pop
{'game': 'BGMI', 'cricketer': 'virat kohli'}
```

### popitem() method

A popitem() method is used to remove data at the end of the dictionary.

*syntex –> dictionary_name.popitem()*

**Example:**

```python
user1 = {'name': 'harshit', 'age': 25, 'state': 'haryana'}
print(user1)

user1.popitem()

print(user1)
```

**Output:**

```markup
{'name': 'harshit', 'age': 25, 'state': 'haryana'}
{'name': 'harshit', 'age': 25}
```

## Loop in dictionary

before applying the loop let’s see some methods of dictionary that are used with the loop.

1. **.keys()** –> gives keys of dictionary
2. **.values()** –> gives values of dictionary
3. **.items()** –> gives keys and values of the dictionary in the form **`[(key1, value1),(key2, value2),...]`**

**print keys of dictionary**

```python
user_info = {'name': 'yash', 'age': 21, 'state': 'Gujarat'}

for i in user_info:
    print(i)

# ******OR********
# for i in user_info.keys():
#     print(i)

```

**Output:**

```markup
name
age
state
```

**print values of dictionary**

Copy

```python
user_info = {'name': 'yash', 'age': 21, 'state': 'Gujarat'}

for i in user_info.values():
    print(i)
```

**Output:**

```markup
yash
21
Gujarat
```

**print both keys and values of dictionary**

```python
user_info = {'name': 'yash', 'age': 21, 'state': 'Gujarat'}

for i,j in user_info.items():
    print(f'{i}:{j}')
```

**Output:**

```markup
name:yash
age:21
state:Gujarat
```

## check if key exists in the dictionary.

```python
user_info = {'name': 'harshit', 'age': 25, 'state': 'haryana'}

if 'age' in user_info:
    print('age is present')
else:
    print('not present')

if 'surname' in user_info:
    print('surname present')
else:
    print('surname is not present')

# You can also use .keys() method to check if key is present or not

if 'age' in user_info.keys():
    print('age is present')
else:
    print('age is not present')
```

**Output:**

```markup
age is present
surname is not present
age is present
```

## check if value exists in the dictionary.

```python
user_info = {'name': 'yash', 'age': 21}

if 'yash' in user_info.values():
    # .values() method check for values
    print('yash is present')
else:
    print('not present')
```

**Output:**

```markup
yash is present
```

## methods of dictionary

| .update() | .fromkeys() | .get() |
| --- | --- | --- |
| .pop() | .popitem() | .clear() |
| .copy() | .items() | .values() |
| .keys() | setdefault() |  |

### update() method

update() method is used to add data in a dictionary but arguments passed in the update method are in the form of a ***key: value*** pair.

**Example:**

```python
user_info = {'name': 'yash', 'age': 21, 'state': 'Gujarat'}

Extra_info = {'fav_movie':'dolittle','hobbies':['reading','writing']}

user_info.update(Extra_info)
print(user_info)
```

**Output:**

```markup
{'name': 'yash', 'age': 21, 'state': 'Gujarat', 'fav_movie': 'dolittle', 'hobbies': ['reading', 'writing']}
```

### fromkeys() method

fromkeys() method is used to create a dictionary with default values.

**Example:**

```python
dictinary = dict.fromkeys(['name','age','hobbies'],'unknown')
print(dictinary)
```

**Output:**

```markup
{'name': 'unknown', 'age': 'unknown', 'hobbies': 'unknown'}
```

### clear() method

clear() method is used to clear data of dictionary.

**Example:**

```python
info = {'name': 'harshit', 'age': 25}

info.clear()
print(info)
```

**Output:**

```markup
{}
```

### copy() method

copy() method is used to create a new copy of the existing dictionary.

**Example:**

```python
info = {'name': 'harshit', 'age': 25}

info2 = info.copy()

print(info2)
```

**Output:**

```markup
{'name': 'harshit', 'age': 25}
```

if you write **`info2 = info`**, this will not create a new copy of the dictionary but it will only create two different names for your dictionary.

### setdefault() method

The **`setdefault()`** method is very similar to the **`get()`** method, but the **`setdefault()`** method creates a new key with a default value if the key is not present in the dictionary.

```python
my_dict = {'a': 1, 'b': 2}

# Using setdefault to set a default value for a key that doesn't exist
result1 = my_dict.setdefault('c', 0)  # 'c' is not in the dictionary, so it's added with a default value of 0
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 0}
print(result1)  # Output: 0

# Using setdefault for a key that already exists
result2 = my_dict.setdefault('a', 10)  # 'a' is already in the dictionary, so its value is not changed
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 0}
print(result2)  # Output: 1 (the existing value associated with 'a')
```

# Dictionary Comprehension

## What is Dictionary Comprehension?

Dictionary comprehension is a short-hand method to create a new dictionary from the existing iterables such as lists, tuples, etc.

It is very similar to list comprehension, with the only difference being that we pass **`key-value`** pairs instead of individual elements in dictionary comprehension.

## Syntax of Dictionary Comprehension

**`{key_expression: value_expression for i in iterable}`**

**For Example:**

Suppose you want to create a dictionary that includes numbers from 1 to 10 as keys and their respective squares as the corresponding values. You can do it in just one line using dictionary comprehension.

```python
square = {num: num**2 for num in range(1,11)}
print(square)
```

**Output:**

```markup
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/b1dbd28a-9a85-45cf-9f11-f160974e1f65/f9617c0d-e623-46eb-b2e6-a0991eb26fbc/Untitled.png)

## Dictionary Comprehension with If Statement

You can also include conditions while creating a dictionary using dictionary comprehension. Let’s understand this concept with the help of an example.

**Syntax:**

**`{key_expression: value_expression for i in iterable if Condition == True}`**

**Example-1:** Create a dictionary that stores even numbers from 1 to 10 as keys and their squares as the corresponding values.

```python
d1 = {num: num**2 for num in range(1,11) if num%2 == 0}
print(d1)
```

**Output:**
