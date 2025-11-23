## Iterator vs iterable vs iteration

Iterable :- An iterable is an object you can loop over

Iterator An iterator is the object that does the looping (or) travers through a sequence of data with out storing the  data in the memory one item at a time

Iteration is the process of looping through elements

Iterarion using the for loop:

```python
data=[10,20,30]

for ele in data:  
    print(ele)
```

It iterates through list and prints each element

10

20

30

### Iterator

Iterators are a fundamental concept in Python that enable you to traverse through all the elements of a collection (like lists, tuples, dictionaries, etc.). They provide a systematic way to access elements sequentially without needing to know the underlying structure of the collection.

### Key Concepts:

- Iterable: Any object that can return an iterator. Examples include lists, tuples, sets, dictionaries, and strings.

```python
my_list = [1, 2, 3]
my_iterable = iter(my_list)
```

- Iterator: An object representing a stream of data; it returns the next item in the sequence when the next() function is called.

```python
print(next(my_iterable))  # Output: 1
print(next(my_iterable))  # Output: 2
print(next(my_iterable))  # Output: 3
```

### Creating an Iterator:

To create an iterator from an iterable, you use the iter() function. Then, you can use next() to access elements one by one.

### Example:

```python
my_tuple = (1, 2, 3)
iterator = iter(my_tuple)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
```

```python
L=[10,20,30,40]
iter_obj=iter(L)  # iterator

print(type(iter_obj))  # <class 'list_iterator'>

# to access elements 
print(next(iter_obj))  # 10
print(next(iter_obj)) # 20
print(next(iter_obj)) # 30
print(next(iter_obj)) #40
print(next(iter_obj)) #  StopIteration exception

```

* we can create an iterator by using iter() abd by passing sn iterable object eg: list,string
* we need next() and by using the iter object to access the element eg: iter_obj (iter object reference)

- next() remembers the state of the iterator, so each call to next() continues from where the last call left off.
- This is why each call to next() returns the subsequent item in the sequence.

  Example:
- Here next() function is used to get the next item from the iterator.
- The first call to next(it) retrieves the first item (1) from the iterator.
- The second call to next(it) retrieves the second item (2) from the iterator.
- The third call to next(it) retrieves the third item (3) from the iterator.
- The fourth call to next(it) retrieves the fourth item (4) from the iterator.
- every time next() is called, it returns the next item in the sequence until there are no more items left.
- When there are no more items to return, a StopIteration exception is raised.

### Example : How a next() knows the current  iteration?

Python creates an **iterator object** with:

* A  **reference to the original list** .
* An **internal index** (starts at 0).

Each time you call `next(iter_obj)`:

* Python looks at `L[index]`.
* Returns that value.
* Increments `index` by 1.
* If `index` exceeds the list length, it raises `StopIteration`.

```python
## next() knows the current iteration

L=[10,20,30,40]

iter_obj=iter(L) # iterator

print(next(iter_obj)) #10
print(next(iter_obj)) # 20

for ele in iter_obj:
    print(ele)       #30
                     # 40
```

### How to check an object is iterable or iterator?

```python

L=[10,20,30,40]

print(dir(L)) # it only contains __iter__  so this is iterable
```

```python
iter_obj=iter(L) 
print(dir(iter_obj)) # It contains __iter__ and __next__ so this is an iterator 
```

### Benefits of Iterators:

- Memory Efficiency: Iterators compute values one at a time, which is memory efficient, especially when working with large datasets.
- Lazy Evaluation: Items are generated as needed, allowing for efficient data processing.
- Simplifies Code: Provides a simple and clean syntax for iterating over sequences.

### Making your own for loop

```python

L=[10,20,30,40]

def for_loop(iterable):
    iterator=iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass
for_loop(L)
```

##### using recursion

```python
def for_loop(iterable):
    iterator = iter(iterable)
  
    def loop():
        try:
            print(next(iterator))
            loop()  # recursive call
        except StopIteration:
            pass

    loop()

# Example
L = [10, 20, 30, 40]
for_loop(L)

```

### Custom Iterators: Creating our own range ()

You can create custom iterators by defining a class with `__iter__()` and  `__next__()` methods.

Example:

```python
class Myrange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


my_iter = Myrange(1, 4)

for value in my_iter:
    print(value)

```

So here is the output

Output:

```
1
2
3
```

### What is an Iterator?

An iterator is an object that implements two special methods: `__iter__()` and `__next__()`. These methods allow you to loop through (or traverse) the elements of a collection like lists, tuples, or even user-defined objects.

### Key Characteristics of Iterators:

- `__iter__() Method`: This method should return the iterator object itself. It's called when an iterator is required for a container.

```python
def __iter__(self):
    return self
```

- `__next__() Method`:  this method returns the next item from the collection. It should raise a StopIteration exception when there are no more items to return.

```python
def __next__(self):
    if condition:
        raise StopIteration
    else:
        return item
```

### Example of a Custom Iterator:

Let's create a simple iterator that counts up to a given number:

```python
class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        else:
            self.current += 1
            return self.current

# Using the custom iterator
counter = CountUpTo(5)
for number in counter:
    print(number)
```

## output:

```
1
2
3
4
5
```

### **Using Custom iterators buid a range() including step**

```python
# range with step
class MyRange:
    def __init__(self,start,end,step=1):
        self.current=start
        self.end=end
        self.step=step

    def __iter__(self):
        return self
  
    def __next__(self):
        if (self.step >0 and self.current>=self.end) or (self.step<0 and self.current<=self.end):
            raise StopIteration
        value=self.current
        self.current+=self.step
        return value
  
    for num in MyRange(1,10,2):
        print(num)
```

### Internal Working:

- Initialization: When you create an instance of CountUpTo, it initializes max and sets current to 0.
- Iteration: The for loop calls __iter__() to get the iterator object, which is itself in this case.
- Fetching Items: The loop then repeatedly calls __next__() to get the next item until StopIteration is raised.

### Built-in Iterators and Iterables:

Python comes with built-in iterables like lists, tuples, dictionaries, and strings, all of which can be converted to an iterator using the iter() function.

```python
my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3

```

### Practical Use Cases:

- File Reading: Efficiently read lines from a file without loading the entire file into memory.

```python

with open('file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

- Data Processing: Handle large datasets or streams of data in a memory-efficient manner.
- Infinite Sequences: Create sequences that theoretically have no end, like the Fibonacci series.

### Iterators vs. Generators:

- Iterators: Require more boilerplate code to define __iter__() and __next__() methods.
- Generators: Simplify the creation of iterators using yield, which handles state and iteration automatically.

````

````
