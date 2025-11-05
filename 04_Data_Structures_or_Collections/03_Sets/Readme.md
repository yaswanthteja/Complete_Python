## What is set in Python?

**The set is a built-in data structure in python and it is used to store an unordered collection of unique items.**

## Use of set in python

- **Set is used to store different data types in python** like integer, string, float, tuple, etc.
- **Set is used to remove duplicate data or items from a list** (it is one of the most important uses of a set).
- **it is used to perform union and intersection between two sets**

**NOTE:** You can not store built-in data structures (like list, dictionary, set, etc.) inside a set except tuple.

if we tried to add list or dict or set it gives Type error unhashable: every value have hash value but in mutables changes the hash value when it is updated so it gives the error.

Because of the mutation of these data structures we can’t store in the set.

Including set , set is mutable but the elements of set are immutable.

## Create Set in python

To create a set in python write a comma separate values inside a curly bracket

( **{ }** ).

**Example:**

```python
# create a set in python
set1 = {1,2,3,4,'five',(1,3,5,7)}
print(set1)

print(type(set1))
```

**Output:**

```markup
{'five', 1, 2, 3, 4, (1, 3, 5, 7)}
<class 'set'>
```

## Create Empty set in python

**you can use the `set()` function to create an empty set in Python** and it is the only way, you can not use **`{ }`** to create an empty set as shown below.



right way to create a empty set in python

**Example:**

```python
my_set1 = set()

print(my_set1)
```

**Output:**

```markup
set()
```

**NOTE:** Set in Python is mutable (means you can add or delete data from the set)

## Add data or item in set

you can use the **.add()** method to add data or items in a set.

**Example:**

```python
my_set1 = set()
# empty set
print(my_set1)

# add data in set
my_set1.add(1)
my_set1.add(3)
my_set1.add(5)
my_set1.add('allinpython')
my_set1.add(5.3)

print(my_set1)
```

**Output:**

```markup
set()
{1, 3, 5.3, 5, 'allinpython'}
```

## Delete data or item from set

you can use the **.remove()** method to delete data or items from the set.

**Example:**

```python
set1 = {1,2,3,4,'five',(1,3,5,7)}
print(set1)

set1.remove((1,3,5,7))
print(set1)

set1.remove('five')
set1.remove(1)
set1.remove(2)
print(set1)

set1.remove(3)
set1.remove(4)
print(set1)
```

**Output:**

```markup
{1, 2, 3, 4, 'five', (1, 3, 5, 7)}
{1, 2, 3, 4, 'five'}
{3, 4}
set()
```

## iterate in a set using for-loop

```python
set2 = {1, 3, 5, 5.3, 'allinpython'}

for i in set2:
    print(i)
```

**Output:**

```markup
1
3
5
5.3
allinpython
```

## Union and intersection in set

there is two ways to find union and intersection in set.

1. by using **.union()** and **.intersection()** method.
2. by using ‘**|**‘ for Union and ‘**&**‘ for an intersection.

### by using and method

```python
s1 = {1,2,3}
s2 = {3,4,5,6,7,8,9}

print('s1 = ',s1)
print('s2 = ',s2)

print('union = ',s1.union(s2))
print('intersection = ',s1.intersection(s2))
```

**Output:**

```markup
s1 =  {1, 2, 3}
s2 =  {3, 4, 5, 6, 7, 8, 9}
union =  {1, 2, 3, 4, 5, 6, 7, 8, 9}
intersection =  {3}
```

### by using ‘‘ for Union and ‘‘ for an intersection

```python
s1 = {1,2,3}
s2 = {3,4,5,6,7,8,9}

print('s1 = ',s1)
print('s2 = ',s2)

s3 = s1 | s2
print('union = ',s3)

s4 = s1 & s2
print('intersection = ',s4)
```

**Output:**

```markup
s1 =  {1, 2, 3}
s2 =  {3, 4, 5, 6, 7, 8, 9}
union =  {1, 2, 3, 4, 5, 6, 7, 8, 9}
intersection =  {3}
```

Let’s see the use of the set in python by doing a program.

## Python program to remove duplicate items from a list

there are three steps to do this program:

**Step-1**: convert the list into a set to remove duplicate items.

**Step-2**: convert the set into a list again.

**Step-3**: print the list.

```python
l1 = [1,1,2,3,4,2,5,6,7,5,4]

# list with duplicate items
print(l1)

s1 = set(l1) # converted into set

l1 = list(s1) # converted into list

# list with no duplicate items
print(l1)
```

**Output:**

```markup
[1, 1, 2, 3, 4, 2, 5, 6, 7, 5, 4]
[1, 2, 3, 4, 5, 6, 7]
```

**you can also write the above program in just one line.**

```python
l1 = [1,1,2,3,4,2,5,6,7,5,4]
print(list(set(l1)))
```

**Output:**

```markup
[1, 2, 3, 4, 5, 6, 7]
```
