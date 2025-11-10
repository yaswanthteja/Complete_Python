### What Are Generators?

Generators are a special type of iterator that allow you to iterate over a sequence of values, but instead of storing all the values in memory, they generate each value on the fly. This makes them memory efficient and ideal for large datasets or infinite sequences.

A **generator** is a function that returns an  **iterator object** . Instead of computing and storing all values at once (like a list), it **yields** values one by one — pausing after each and resuming when needed.

### The yield Keyword

The yield keyword is used inside a generator function. **It pauses the function and saves its state** so that it can be resumed later. Each time the yield statement is encountered, the function outputs the value specified and retains its state for the next iteration.

- yield allows for lazy evaluation, where values are produced and processed as needed. This is useful for scenarios where you do not need all the data at once.

Generators using yield provide a simpler way to create iterators compared to defining a class with __iter__() and __next__() methods.


```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1



```

```python
# Simplified version using yield
def counter(max):
    current = 1
    while current <= max:
        yield current
        current += 1

# Using the generator
for num in counter(5):
    print(num)
```

### Generator vs Regular Function


| Feature      | Generator (`yield`)       | Regular Function (`return`) |
| ------------ | --------------------------- | ----------------------------- |
| Returns      | One value at a time         | One final value               |
| Memory usage | Low (no full list stored)   | High (stores all values)      |
| Execution    | Pauses and resumes          | Ends after return             |
| Use case     | Large/infinite data streams | Simple, one-time results      |




### How Generators Work:

**Generator Function:** Defined like a regular function but uses yield instead of return.

**Yielding Values:** When the generator is iterated, it produces values one at a time, pausing after each yield and resuming from there when called again.



## How It Works Internally

* When the generator function is called, it  **does not run immediately** .
* It returns a **generator object** that remembers:
  * The function’s code
  * The current position
  * All local variables
* Each call to `next()` resumes execution **right after the last **`yield`, continuing until the next `yield` or `StopIteration`.

This behavior is called **lazy evaluation** — values are computed only when needed



### Why we use yield instead of return??

the behavior of the return statement in a function. When a return statement is executed, **it immediately exits the function and returns the specified value.** Any code after the first return statement is not executed.

```python
def foo():
    return 1
    return 2
    return 3

print(foo())  # Output: 1


```

First return: The function encounters return 1 and exits, returning 1.

Subsequent return Statements: They are never reached or executed.

In this case, the output will always be 1 because the function returns as soon as it hits the first return statement, ignoring any code that follows. This showcases that a function can only return one value and exits right after the return statement is executed

#### yield

When you call this function and iterate over it, **it will produce values one at a time, pausing and resuming at each yield statement.**


```python
def foo():
    yield 1
    yield 2
    yield 3

# Creating a generator object
gen = foo()  # <generator object foo at 0x000001B370A6E610>
```



When you call foo(), it doesn't execute the function immediately. Instead, it returns a generator object.

- So here we have object by using for loop we can iterate through it.

```python
def foo():
    yield 1
    yield 2
    yield 3

# Creating a generator object
gen = foo()

# Iterating over the generator
for value in gen:
    print(value)


```

### Output:

```
1
2
3
```


- Generator Creation: When you call foo(), it doesn't execute the function immediately. Instead, it returns a generator object.
- Iteration: Each time you iterate over the generator (e.g., using a for loop or calling next()), it resumes execution from the last yield statement.
- State Preservation: The generator maintains its state between calls, allowing it to continue from where it left off.

This approach is particularly useful for handling sequences of data efficiently, as it generates values on-demand without needing to store the entire sequence in memory. Pretty handy

### Simple Example:

Let's create a simple generator that generates numbers from 0 up to a given limit.

```python
def simple_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

gen = simple_generator(5)
for number in gen:
    print(number)
```

### Output:

```
0
1
2
3
4
```

- The function simple_generator is defined with yield instead of return.
- Each time yield i is called, the value of i is produced, and the function’s state is saved.
- When the generator is iterated, it picks up where it left off and continues until the condition i < n is no longer true.



### Advanced Example: Fibonacci Sequence

Here's a generator for the Fibonacci sequence:

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))
```

### Output:

```
0
1
1
2
3
5
8
13
21
34
```

### Benefits of Generators:

- Memory Efficiency: Only one item is generated and stored at a time.
- Infinite Sequences: Perfect for sequences that can theoretically go on forever, such as Fibonacci numbers.
- Lazy Evaluation: Values are produced only when needed, making operations more efficient.

Generators, with their ability to yield values one at a time, offer a powerful tool for managing large datasets and implementing complex iterations elegantly. They simplify code and enhance performance, particularly when dealing with large or infinite sequences.




## Real-World Use Cases

* **Reading large files line by line**
* **Streaming data from APIs**
* **Generating infinite sequences**
* **Filtering or transforming data on the fly**
