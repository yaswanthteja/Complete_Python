## What is tuple in python?

A tuple is a built-in ordered data structure in python and it is used to store a collection of items like integer, float, string, list, dictionary, set, etc in one variable.

**NOTE:** Once a tuple is created you can not update or modify it because the tuple is immutable.

## Why do we use tuple?

If we compare the list with tuple then yes list has much more flexibility **but tuple is much faster than the list and this is the primary reason to use a tuple.**

second reason sometimes we don’t need to update our data and that time tuple is the best choice to use instead of a list.


# Tuple Data Structure

1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple 
object,we cannot perform any changes in that object.
Hence Tuple is Read Only version of List.
2. If our data is fixed and never changes then we should go for Tuple.
3. Insertion Order is preserved
4. Duplicates are allowed
5. Heterogeneous objects are allowed.
6. We can preserve insertion order and we can differentiate duplicate objects by using 
index. Hence index will play very important role in Tuple also.
Tuple support both +ve and -ve index. +ve index means forward direction(from left to 
right) and -ve index means backward direction(from right to left)
7. We can represent Tuple elements within Parenthesis and with comma seperator.
 Parenethesis are optional but recommended to use.





## Create tuple in python

To create a tuple in python write comma-separated values inside the parenthesis (small brackets).

**Example:**

```python
t1 = (1,3,5,7,'saurabh',5.3) # create a tuple
print(t1)
```

**Output:**

```markup
(1, 3, 5, 7, 'saurabh', 5.3)
```

## Tuple creation:

 1. creation of empty tuple
 ```
 t=(10,)
 ```
 t=10,
 creation of single valued tuple ,parenthesis are optional,should ends with comma

```
 t=(10,20,30)
```
 creation of multi values tuples & parenthesis are optional
### 4. By using tuple() function:

```
list=[10,20,30] 
t=tuple(list) 
print(t) 

t=tuple(range(10,20,2)) 
print(t) 

```
Example:

 ```
t=10,20,30,40 
print(t) 
print(type(t)) 

Output
(10, 20, 30, 40) 
<class 'tuple'> 

t=() 
print(type(t)) # tuple 
 ```

Note: We have to take special care about single valued tuple.compulsary the value 
should ends with comma,otherwise it is not treated as tuple.

Eg:

```

t=(10) 
print(t) 
print(type(t)) 

Output 
10 
<class 'int'> 
```
```
# Q. Which of the following are valid tuples?
 t=()
 t=10,20,30,40
 t=10
 t=10,
 t=(10)
 t=(10,)
 t=(10,20,30,40)
```



## Access elements of tuple

We can access either by index or by slice operator

```
1. By using index:

t=(10,20,30,40,50,60) 
print(t[0]) #10 
print(t[-1]) #60 
print(t[100]) IndexError: tuple index out of range 

2.By using slice operator:

t=(10,20,30,40,50,60) 
print(t[2:5]) 
print(t[2:100]) 
print(t[::2]) 

Output
(30, 40, 50) 
(30, 40, 50, 60) 
(10, 30, 50) 
```

You can access elements of a tuple by using indexing.

Indexing starts from **0** (ZERO) and ends at **len(tuple) – 1**.

**Example:**

```python
t1 = (1,3,5,7,'allinpython',5.3)

# access 1 ----> index value of 1 is 0

print(t1[0])

# access allinpython ---> index value of allinpython is 4

print(t1[4])

# access last elements of tuple
print(t1[-1])
```

**Output:**

```markup
1
allinpython
5.3
```

| t1 (values) | positive index values | negative index values |
| --- | --- | --- |
| 1 | 0 | -6 |
| 3 | 1 | -5 |
| 5 | 2 | -4 |
| 7 | 3 | -3 |
| allinpython | 4 | -2 |
| 5.3 | 5 | -1 |







## Loop in tuple

### Iterate in a tuple using while-loop

**Example:**

```python
t2 = (45,45.6,23,67,12.1)

i = 0
while i< len(t2):
    print(t2[i])
    i+=1
```

**Output:**

```markup
45
45.6
23
67
12.1
```

### Iterate in a tuple using for-loop

```python
t2 = ('harsh',201,21,'football')
for i in t2:
    print(i)
```

**Output:**

```markup
harsh
201
21
football
```

## Tuple with one element



To create a tuple with a single element put a comma after your value otherwise it is not considered a tuple element.

**Example:**

```python
t3 = (2)
print(t3)
print(type(t3)) #---> return int not tuple

t3 = (2,)
print(t3)
print(type(t3)) #---> return tuple
```

**Output:**

```markup
2
<class 'int'>
(2,)
<class 'tuple'>
```

## Tuple without parenthesis

To create a tuple without using parenthesis write a comma-separated value after assigning your variable.

**Example:**

```python
guitars = 'yamaha','bataon rouge','taylor'
print(guitars)
print(type(guitars))
```

**Output:**

```markup
('yamaha', 'bataon rouge', 'taylor')
<class 'tuple'>
```

## Tuple unpacking



Tuple unpacking means you can store every element of a tuple in different-different variables.

**Example:**

```python
# create a tuple
guitarists = ('moneti jamal', 'eddie van der meer','andrew foy')

# tuple unpacking

guitarists_1,guitarists_2, guitarists_3 = guitarists

print(guitarists_1)
print(guitarists_3)
```

**Output:**

```markup
moneti jamal
andrew foy
```

**NOTE:** If the number of variables is less or more than the value present inside a tuple then it will give an error.





## Tuple vs immutability:
Once we creates tuple,we cannot change its content.
Hence tuple objects are immutable.
 
Eg:
```
t=(10,20,30,40)
t[1]=70 TypeError: 'tuple' object does not support item assignment
```


## Important functions/methods of Tuple:
## 1. len()
 To return number of elements present in the tuple
 Eg:
 ```
 t=(10,20,30,40)
 print(len(t)) #4
```
## 2. count()
 To return number of occurrences of given element in the tuple
 Eg:
 ```
 t=(10,20,10,10,20)
 print(t.count(10)) #3
 ```

count() method counts the number of times a specified value presents in the tuple.

**Example:**

```python
t2 = (45,45.6,23,67,12.1,23,45.6,23)

count1 = t2.count(23)
print(count1)

count2 = t2.count(45.6)
print(count2)
```

**Output:**

```markup
3
2
```

## 3. index()
 returns index of first occurrence of the given element.
 If the specified element is not available then we will get ValueError.
 Eg:
 ```
 t=(10,20,10,10,20)
 print(t.index(10)) #0
 print(t.index(30)) ValueError: tuple.index(x): x not in tuple
 ```
index() method returns index value of specified element.

**Example:**

```python
guitars = ('yamaha','bataon rouge','taylor')

index_1 = guitars.index('bataon rouge')
print(index_1)
```

**Output:**

```markup
1
```

## 4. sorted()
 To sort elements based on default natural sorting order
 ```
t=(40,10,30,20) 
t1=sorted(t) 
print(t1) 
print(t) 

Output
[10, 20, 30, 40] 
(40, 10, 30, 20) 
```
We can sort according to reverse of default natural sorting order as follows
```
t1=sorted(t,reverse=True)
print(t1) [40, 30, 20, 10]
```

## 5. min() and max() functions:
These functions return min and max values according to default natural sorting order.
Eg:

```
1. t=(40,10,30,20) 
2. print(min(t)) #10 
3. print(max(t)) #40 
6. cmp():
```
- It compares the elements of both tuples.
- If both tuples are equal then returns 0
- If the first tuple is less than second tuple then it returns -1
- If the first tuple is greater than second tuple then it returns +1
 Eg:
```
t1=(10,20,30) 
t2=(40,50,60) 
t3=(10,20,30) 
print(cmp(t1,t2)) # -1 
print(cmp(t1,t3)) # 0 
print(cmp(t2,t3)) # +1 
```
Note: cmp() function is available only in Python2 but not in Python 3





## List inside a tuple

list present inside a tuple is act like a normal list which means you can update or delete elements of the list (you can use every methods of the list like .pop(), .append(), etc.,).

**Example:**

```python
t4 = (4,7,3,['rocky','yashin','malik'])

print(t4)

# access list present inside tuple
print(t4[3])

# delete last eleemnt of list
t4[3].pop()
print(t4)

# add in list
t4[3].append('roja')

print(t4)

# clear list
t4[3].clear()

print(t4)
```

**Output:**

```markup
(4, 7, 3, ['rocky', 'yashin', 'malik'])
['rocky', 'yashin', 'malik']
(4, 7, 3, ['rocky', 'yashin'])
(4, 7, 3, ['rocky', 'yashin', 'roja'])
(4, 7, 3, [])
```

## Function returns two values in the form of a tuple

**Example:**

```python
def func(a,b):
    add1 = a+b
    mul1 = a*b
    return add1,mul1

print(func(3,5))

add1, mul1 = func(2,7)  #tuple unpacking

print(add1)
print(mul1)
```

**Output:**

```markup
(8, 15)
9
14
```

## Create a tuple with range function

**Example:**

```python
nums = tuple(range(1,11))
print(nums)
```

**Output:**

```markup
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

### WAP to count no of students with grade "A" in the following tuple

```python
tup=('C','D','A','A','B','B','A')
print(tup.count('A'))
```








