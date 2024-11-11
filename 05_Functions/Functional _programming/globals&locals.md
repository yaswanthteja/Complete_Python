    

    

## globals() & locals() function

symbol table: It is a data structure which contains all necessary  information about global space of the program

### global()

globals() returns a dictionary of current global symbol table.

Syntax:

```python
globals()
```

ex:

```python
a=10
def demo():
	print('hello')
print(globals())
```

output:

```python
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000001FDF5DC4350>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:\\python_programs\\main.py', '__cached__': None, 'a': 10, 'demo': <function demo at 0x000001FDF5F38900>}
```

```python
a=10
def demo():
	print('hello')
	globals()['a']=10000

demo()
print(a)
```

```python
hello
10000
```

## locals()

**`locals()`** is a built-in function that returns a dictionary containing the current local symbol table. The local symbol table is a namespace containing the names of local variables, which includes variables defined in the current function and any variables passed as arguments.

```python
a=10
def demo():
	print('hello')
	b=100
	print(locals())
demo()
```

```python
hello
{'b': 100}
```

```python
a=10
def demo():
	print('hello')
	b=100
	print(locals()['b'])
demo()
```

```python
hello
100
```

## non-local


The nonlocal keyword in Python is used to work with variables inside nested functions, where the variable should not belong to the inner function. It allows you to modify a variable in the outer (non-global) scope.

nonlocal keyword is used to indicate that a variable is not local to the current functions's scope but reffer's to a variable in the nearest enclosing(non-global) scope.

### example: 
When you have a nested function and you want to modify a variable defined in the outer function, but it isn't global, nonlocal comes into play.

```
def outer_function():
    x = "Hello"
    
    def inner_function():
        nonlocal x
        x = "Hi"
        print("Inner:", x)
    
    inner_function()
    print("Outer:", x)

outer_function()

```

### output:

```
Inner: Hi
Outer: Hi

```

- outer_function(): This is the outer function where x is initially set to "Hello".

- inner_function(): This is the nested function where we use nonlocal to indicate that x refers to the variable in outer_function.

- nonlocal x: Without nonlocal, x inside inner_function would be treated as a local variable, and changes to it would not affect the x in outer_function.

- The nonlocal keyword is essential for cases where you need to change the state of a variable from within a nested function, but that variable isn't global. It's quite handy for maintaining state in closures and more complex function structures!

