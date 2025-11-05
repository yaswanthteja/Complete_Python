return = statement used to end a function call and send a result back to the caller

It stops the function's execution and optionally passes back a result.


Example:

```python
def add(a, b):
    return a + b

```


* Ends the function execution.
* Sends the result (`a + b`) back to wherever the function was called.


Returning multiple values


```python
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = stats([1, 2, 3])

```

Returning Nothing 

If no value is specified, Python returns `None` by default:

```python
def greet():
    print("Hello")
    return

print(greet())  # Output: Hello \n None

```

so every time if a function doesn't have any return type it will return none by default and if the function only have print statement then also it will  print the value and there is no return statement so it gives none


```python

def greet():
    print("Hello")

result = greet()
print(result)  # Output: Hello \n None

```


* `print("Hello")` runs inside the function.
* `result` gets assigned the return value of `greet()` — which is `None`.


so if the function doesn't have any return type and only print statement when we call the function with out reference then it only prints the value


```python
def greet(wish):
    print(wish)

greet("hello")
```



* **What happens** :
* `"hello"` is printed to the screen.
* The function doesn’t return anything, so its return value is `None`.
* **But since you're not storing or printing the return value** , you only see: hello


If You Do Use a Reference

```python
def greet(wish):
    print(wish)

result = greet("hello")
print(result)
```

output

hello
None


* `"hello"` is printed inside the function.
* `result` is assigned the return value of `greet()` → which is `None`.
* `print(result)` shows `None`.


```python
def greet(wish):
    print(wish)

greet("hello")

print(greet("hello"))
```


if we print the function directly then also we can get printed value and  none




### Rule of Thumb

> If a function only prints and has no `return`, calling it directly will  **only show the printed output** .
> If you store its result and print that, you'll see the printed output **plus **`None`.
