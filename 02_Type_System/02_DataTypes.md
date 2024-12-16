### Literals

In programming, **literals are fixed values** (**actual values**) you can use directly in your code. They are the simplest form of an expression. Here’s a quick rundown:
 Python has a wide variety of literals. These include:

- Integer Literals: Whole numbers, e.g., 100.
- Float Literals: Numbers with a decimal point, e.g., 3.14.
- String Literals: Text enclosed in quotes, e.g., "Hello", 'World'.
- Boolean Literals: Truth values, True or False.
- None Literal: Represents the absence of a value, None.
- Complex Literals: Represent complex numbers, e.g., 3 + 4j.

They’re essential because they allow you to provide constant values in your code directly.

## Difference between literals and data types??

Literals and data types are fundamental in programming but serve different purposes:

### **Literals**

* **Definition** : Specific, fixed values directly written in the code.
* **Examples** : `42` (integer), `3.14` (float), `"Hello"` (string), `True` (boolean).
* **Usage** : Represent constant values in code.

### **Data Types**

* **Definition** : Categories that define the kind of data a variable can hold.
* **Examples** : `int` (integer), `float` (floating-point number), `str` (string), `bool` (boolean).
* **Usage** : Determine the operations that can be performed on data and the memory needed.

#### Example:

In short, literals are the actual values you assign to variables, while data types define the kind of values a variable can hold. It’s like how a car’s model is a “literal” Ford Mustang, and its category, like sedan or convertible, is its “data type.”

# Data Types

**Data types** define the kind of data a variable can hold.

In Python, data types can be classified into two broad categories: primitive types (also known as primitive data types) and non-primitive types (also known as composite or derived data types).

## Primitive Types:

Primitive types in Python are the fundamental data types that are not composed of other data types. They are built-in and directly supported by the language. The primitive types include:

- Numeric types: `int`, `float`, `complex`
- Text type: `str`
- Boolean type: `bool`
- Primitive types are immutable, which means their values cannot be changed once they are assigned.

## Non-Primitive Types:

Non-primitive types are data types that are composed of multiple primitive or non-primitive types. They are also known as composite or derived data types. Some common non-primitive types include:

- Sequence types: `list`, `tuple`, `range`
- Mapping type: `dict`
- Set types: `set`, `frozenset`

Non-primitive types are generally mutable, meaning their values can be modified after they are created.

# Data Types

Python has several built-in data types to represent different kinds of values. Here are some of the fundamental data types in Python:

1. **Numeric Types:**

   - **`int`:** Integer type represents whole numbers, e.g., 10, -3, 42.
   - **`float`:** Float type represents floating-point numbers, e.g., 3.14, -0.5, 2e10.

   ```python
   integer_number = 42
   float_number = 3.14
   ```

2.**Boolean Type:**

- **`bool`:** Boolean type represents boolean values **`True`** or **`False`**.

  Example:

  ```python
    is_python_fun = True
    is_learning = False
  ```

3. **Text Type:**

   - **`str`:** String type represents sequences of characters enclosed in single or double quotes.

   Example:

   ```python

   message = 'Hello, World!'

   ```
4. **Sequence Types:**

   - **`list`:** List type represents ordered sequences of values, and it is mutable (can be modified).
   - **`tuple`:** Tuple type represents ordered sequences of values, and it is immutable (cannot be modified).
   - **`range`:** Range type represents sequences of numbers, often used in loops.

   Examples:

   ```python

   my_list = [1, 2, 3, 4]
   my_tuple = (10, 20, 30)
   my_range = range(0, 5)

   ```
5. **Mapping Type:**

   - **`dict`:** Dictionary type represents key-value pairs, where each key must be unique.

   Example:

   ```python

   student = {'name': 'Alice', 'age': 25, 'grade': 'A'}

   ```
6. **Set Types:**

   - **`set`:** Set type represents an unordered collection of unique elements.
   - **`frozenset`:** Frozenset type is an immutable version of a set.

   Examples:

   ```python

   my_set = {1, 2, 3}
   my_frozenset = frozenset([4, 5, 6])

   ```
7. **Binary Types:**

   - **`bytes`:** Bytes type represents sequences of bytes and is immutable.
   - **`bytearray`:** Bytearray type represents sequences of bytes and is mutable.
   - **`memoryview`:** Memoryview type represents a view of the memory, mainly used with **`bytes`**.

   Examples:

   ```python

   binary_data = b'Hello'
   mutable_binary_data = bytearray(b'World')

   ```
8. **None Type:**

   - **`None`:** Represents the absence of a value or a null value.

   Example:

   ```python

   no_value = None

   ```

These are the core data types in Python. Understanding these types is fundamental to working effectively with Python's powerful and flexible features.

- Data Type represent the type of data present inside a variable.
- In Python we are not required to specify the type explicitly. Based on value provided,the
  type will be assigned automatically.Hence Python is Dynamically Typed Language.

Python contains the following inbuilt data types

1. int
2. float
3. complex
4. bool
5. str
6. bytes
7. bytearray
8. range
9. list
10. tuple
11. set
12. frozenset
13. dict
14. None

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/584b9b1a-67b5-48e6-b353-b63369dfc49a)

`Note:` Python contains several inbuilt functions

1. ctype()
   to check the type of variable
2. id()
   to get address of object
3. print()
   to print the value

- In Python everything is object

## int data type:

We can use int data type to represent whole numbers (integral values)

- Eg:
  ```
  >>>  a=10
   >>> type(a) #int
  ```

`Note:`

- In Python2 we have long data type to represent very large integral values.
- But in Python3 there is no long type explicitly and we can represent long values also by
  using int type only.

We can represent int values in the following ways

1. Decimal form
2. Binary form
3. Octal form
4. Hexa decimal form

- `Decimal form(base-10):`
  It is the default number system in Python
  The allowed digits are: 0 to 9
  Eg: a =10
- `Binary form(Base-2):`
  The allowed digits are : 0 & 1
  Literal value should be prefixed with 0b or 0B
  Eg:

```
a = 0B1111
 a =0B123
 a=b111
```

- `Octal Form(Base-8):`
  The allowed digits are : 0 to 7
  Literal value should be prefixed with 0o or 0O.

Eg:

```
a=0o123
a=0o786
```

- `Hexa Decimal Form(Base-16):`
  The allowed digits are : 0 to 9, a-f (both lower and upper cases are allowed)
  Literal value should be prefixed with 0x or 0X
  Eg:

```
 a =0XFACE
 a=0XBeef
 a =0XBeer
```

- `Note:` Being a programmer we can specify literal values in decimal, binary, octal and hexa
  decimal forms. But PVM will always provide values only in decimal form.

```
 >>> a=10
 >>> b=0o10
 >>> c=0X10
 >>> d=0B10
 >>> print(a)  #output 10
 >>> print(b)  #output 8
 >>> print(c)   #output 16
 >>> print(d)   #output 2
```

## Base Conversions

- Python provide the following in-built functions for base conversions

1.`bin():`
We can use bin() to convert from any base to binary
Eg:

```
  >>> bin(15)   #output '0b1111' 
  >>> bin(0o11)  #output '0b1001' 
  >>> bin(0X10)  #output '0b10000' 
```

2. `oct():`
   We can use oct() to convert from any base to octal
   Eg:

```
 >>> oct(10) #output '0o12' 
 >>> oct(0B1111) #output '0o17' 
  >>> oct(0X123) #output '0o443' 
```

3. `hex():`
   We can use hex() to convert from any base to hexa decimal
   Eg:

```
 >>> hex(100) #output '0x64' 
 >>> hex(0B111111) #output '0x3f' 
 >>> hex(0o12345) #output '0x14e5' 
```

## float data type:

We can use float data type to represent floating point values (decimal values) which are real numbers (ex: 2.3,1.4 )

In most the programming languages the numbers are stored in 64 bits which is used to equivaltent to  2^64 , ranging from  (0 to 2^64-1)
ex:

#### What are Floating Point Numbers?

Floating point numbers are a way to represent real numbers (numbers with fractional parts) in computing. They consist of three parts: the sign bit, the exponent, and the mantissa (or significand).

```
0.1+0.2  // not 0.3
```

```
0.30000000000000004
```

#### Converting into Decimal to binary

![1734352293852](image/02_DataTypes/1734352293852.png)

#### Converting Binary to decimal

![1734352468959](image/02_DataTypes/1734352468959.png)

Here why it is not 0.3,because 0.1 it converted into base2 and store the value and the same way 0.2 is also stored into base2 and then the result in binary

#### Why 0.1 is Not Equal to 0.1 in Python

This might sound strange, but let me explain. Computers use binary (base-2) system for computation, and not all decimal numbers can be represented exactly as binary fractions. The number 0.1 is one such example. In binary, 0.1 becomes an infinite repeating fraction:

```
0.000110011001100110011001100...
```

When Python (or any other programming language) tries to store this number, it can only store a finite number of digits. This leads to a slight approximation rather than an exact representation.

#### Precision Loss

When performing arithmetic operations with floating point numbers, these small approximations can lead to precision loss. Here's a simple example:

```
x = 0.1 + 0.2
print(x == 0.3)  # This will return False
print(x)        # This will print 0.30000000000000004

```

- Floating-point decimal values generally do not have an exact binary representation. This is a side effect of how the CPU represents floating point data. For this reason, you may experience some loss of precision, and some floating-point operations may produce unexpected results.
- Binary approximation refers to the way computers represent decimal numbers in the binary (base-2) system. Unlike humans who use the decimal (base-10) system, computers use binary because it is simpler and more reliable for digital circuitry.

#### Why Some Numbers Can't Be Represented Exactly

- In the decimal system, we are used to numbers being represented with digits from 0 to 9. In binary, only the digits 0 and 1 are used. This can make it challenging to represent certain decimal numbers exactly.
- For example, the number 0.1 cannot be precisely represented in binary. Here's why:
- In decimal, 0.1 is a straightforward fraction (1/10).
- In binary, 0.1 is equivalent to an infinite repeating fraction: 0.000110011001100110011001100...
- Computers can only store a finite number of digits, so they have to truncate or round off this infinite sequence. This truncation leads to a slight approximation rather than an exact value.

#### Handling Precision Issues

To handle precision issues with floating point numbers in Python, you can use the decimal module which provides decimal floating point arithmetic with more precision and control over rounding.

Here's an example of using the decimal module:

```
from decimal import Decimal

x = Decimal('0.1') + Decimal('0.2')
print(x == Decimal('0.3'))  # This will return True
print(x)                    # This will print 0.3

```

By using Decimal, you can represent decimal numbers exactly and avoid the precision issues associated with binary floating point representation.

Python uses IEEE 754 Standard ,which tells how number should be stored in binary .

Eg:

```
 >>> f=1.234 
 >>> type(f) #output float
```

We can also represent floating point values by using exponential form (scientific notation)
Eg:

```
 >>> f=1.2e3
 >>> print(f) #output 1200.0 
```

- instead of 'e' we can use 'E'
- The main advantage of exponential form is we can represent big values in less memory.
  ***Note:
  We can represent int values in decimal, binary, octal and hexa decimal forms. But we can
  represent float values only by using decimal form.
  Eg:

```
 >>> f=0B11.01 
 File "<stdin>", line 1 
 >>> f=0B11.01
  ^ 
 SyntaxError: invalid syntax 

 >>> f=0o123.456 
 SyntaxError: invalid syntax 
 
 >>> f=0X123.456 
 SyntaxError: invalid syntax 


```

## Complex Data Type:

A complex number is of the form.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/1402ef57-5b44-40e3-ab89-65c29e43f47a)

- a and b contain integers or floating point values
- Eg:

  - 3+5j
  - 10+5.5j
  - 0.5+0.1j
- In the real part if we use int value then we can specify that either by decimal,octal,binary
  or hexa decimal form.
- But imaginary part should be specified only by using decimal form.

```
 >>> a=0B11+5j 
 >>> a 
   (3+5j) 
 >>> a=3+0B11j 
 SyntaxError: invalid syntax 
```

```
Even we can perform operations on complex type values.
 >>> a=10+1.5j 
 >>> b=20+2.5j 
 >>> c=a+b 
 >>> print(c) 
 (30+4j) 
 >>> type(c) 
 <class 'complex'> 
```

- `Note:` Complex data type has some inbuilt attributes to retrieve the real part and
- ** imaginary part **

```
c=10.5+3.6j
c.real==>10.5
c.imag==>3.6
```

- We can use complex type generally in scientific Applications and electrical engineering
  Applications.

## bool data type:

- We can use this data type to represent boolean values.
- The only allowed values for this data type are:
  `True and False`
- Internally Python represents True as 1 and False as 0
  ``b=True type(b) =>bool``
  Eg:

```
 >>> a=10
 >>> b=20
 >>> c=a<b
 >>> print(c)==>True
 >>> True+True==>2
 >>> True-False==>1
```

## str type:

- str represents String data type.
- A String is a sequence of characters enclosed within single quotes or double quotes.

```
s1='durga'
s1="durga"
```

- By using single quotes or double quotes we cannot represent multi line string literals.

```
s1="durga

soft"
```

- For this requirement we should go for triple single quotes(''') or triple double quotes(""")

```
s1='''durga
 soft'''
s1="""durga
 soft"""
```

- We can also use triple quotes to use single quote or double quote in our String.

```
''' This is " character'''
' This i " Character '
```

- We can embed one string in another string

```
'''This "Python class very helpful" for java students'''
```

## Slicing of Strings:

- slice means a piece

- [ ] operator is called slice operator,which can be used to retrieve parts of String.

- In Python Strings follows zero based index.
- The index can be either +ve or -ve.
- +ve index means forward direction from Left to Right
- -ve index means backward direction from Right to Left

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/a67b0cba-073e-48f7-9806-412f9d239447)

```
>>> s="durga" 
>>> s[0] 
 'd' 
 >>> s[1] 
 'u' 
 >>> s[-1] 
 'a' 
 >>> s[40] 
IndexError: string index out of range

>>> s[1:40] 
'urga' 
 >>> s[1:] 
 'urga' 
 >>> s[:4] 
 'durg' 
 >>> s[:] 
 'durga' 
 >>> s*3 
 'durgadurgadurga'  
 >>> len(s) 
   5
```

`Note:`

1. In Python the following data types are considered as Fundamental Data types
   - int
   - float
   - complex
   - bool
   - str
2. In Python,we can represent char values also by using str type and explicitly char type is
   not available.
   Eg:

```
>>> c='a' 
>>> type(c) 
  <class 'str'> 
```

3. long Data Type is available in Python2 but not in Python3. In Python3 long values also
   we can represent by using int type only.
4. In Python we can present char Value also by using str Type and explicitly char Type is
   not available.
