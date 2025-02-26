## String Data Type

The most commonly used object in any project and in any programming language is String only.

Hence we should aware complete information about String data type.

## What is String?

Any sequence of characters within either single quotes or double quotes is considered as a String.

`Syntax`:

```
s='python'
s="python"
```

`Note`: In Python single quotes and double quotes both are exactly same. There is no difference between

`Note2`: In most of other languages like C, C++,Java, a single character with in single quotes is treated.as char data type value. But in Python we are not having char data type.Hence it is treated as String only.

Eg:

```
>>> ch='a'
>>> type(ch)
<class 'str'>
```

## How to define multi-line String literals:

We can define multi-line String literals by using triple single or double quotes.

Eg:

```
>>> s='''we 
are learning
python'''

```

We can also use triple quotes to use single quotes or double quotes as symbol inside String literal.

Eg:

```
s='This is ' single quote symbol' ==>invalid
s='This is \' single quote symbol' ==>valid
s="This is ' single quote symbol"====>valid
s='This is " double quotes symbol' ==>valid
s='The "Python " is 'very' easy' ==>invalid
s="The "Python " is 'very' is easy"==>invalid
s='The \"Python \" is \'very\' is easy' ==>valid
s='''The "Python " is 'very' is easy''' ==>valid
```

## How to access characters of a String:

We can access characters of a string by using the following ways.

1. By using index
2. By using slice operator

## 1. By using index:

Python supports both +ve and -ve index.

- +ve index means left to right(Forward direction)
- -ve index means right to left(Backward direction)

Eg:
s='python'

Eg:

```
>>> s='python'
>>> s[0]
'p'
>>> s[-1]
'n'
>>> s[::-1]
'nohtyp'
>>> s[10] 
IndexError: string index out of range
```

`Note`: If we are trying to access characters of a string with out of range index then we will get error saying : IndexError

Accesing from (-)ve index

```python-repl
num='0123456789'
num[-2:-6]
```

Output

```python-repl
''
```

It will return empty string

Slicing works like this: `String[start:stop:step]`. **When you slice from a higher index to a lower index, the default step is `1`, so it can't go backwards unless you specify a negative step.**

So `num[-2:-6]` essentially means “start at the second-to-last element and go up to, but not including, the sixth-to-last element,” but since it can't move backwards with the default step, it returns nothing.

To slice backwards, use a negative step:

```python
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[-2:-6:-1])  

# Outputs: [8, 7, 6, 5]
```

<br/>

# Assignment

1.Write a program to accept some string from the keyboard and display its characters by index wise(both positive and nEgative index)

## 2. Accessing characters by using slice operator:

`Syntax: s[beginindex:endindex:step]`

- beginindex:From where we have to consider slice(substring)
- endindex: We have to terminate the slice(substring) at endindex-1
- step: incremented value.

`Note`: If we are not specifying begin index then it will consider from beginning of the string.

If we are not specifying end index then it will consider up to end of the string

The default value for step is 1
Eg:

```
1) >>> s="Learning Python is very very easy!!!" 
2) >>> s[1:7:1] 
3) 'earnin' 
4) >>> s[1:7] 
5) 'earnin' 
6) >>> s[1:7:2] 
7) 'eri' 
8) >>> s[:7] 
9) 'Learnin' 
10) >>> s[7:] 
11) 'g Python is very very easy!!!' 
12) >>> s[::] 
13) 'Learning Python is very very easy!!!' 
14) >>> s[:] 
15) 'Learning Python is very very easy!!!' 
16) >>> s[::-1] 
17) '!!!ysae yrev yrev si nohtyP gninraeL' 
```

## Behaviour of slice operator:

`s[begin:end:step]`

- step value can be either +ve or –ve
- if +ve then it should be forward direction(left to right) and we have to consider begin to end-1
- if -ve then it should be backward direction(right to left) and we have to consider begin to end+1

 **Note**:

- In the backward direction if end value is -1 then result is always empty.
- In the forward direction if end value is 0 then result is always empty.

## In forward direction:

- default value for begin: 0
- default value for end: length of string
- default value for step: +1

## In backward direction:

- default value for begin: -1
- default value for end: -(length of string+1).

``Note``: Either forward or backward direction, we can take both +ve and -ve values for begin and
end index.

## Mathematical Operators for String:

We can apply the following mathematical operators for Strings.

1. " + "  operator for concatenation
2. " * " operator for repetition

```
print("HELLO"+"WORLD") 
#HELLOWORLD
print("hello"*2) 
#hellohello
```

`Note: `

1. To use + operator for Strings, compulsory both arguments should be str type
2. To use * operator for Strings, compulsory one argument should be str and other argument should be int

## len() in-built function:

We can use len() function to find the number of characters present in the string.
Eg:'

```
s='python'
print(len(s)) #
6
```

<br/>

## To check type of characters present in a string:

Python contains the following methods for this purpose.

1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
3) isdigit(): Returns True if all characters are digits only( 0 to 9)
4) islower(): Returns True if all characters are lower case alphabet symbols
5) isupper(): Returns True if all characters are upper case aplhabet symbols
6) istitle(): Returns True if string is in title case
7) isspace(): Returns True if string contains only spaces

<br/>

```python
s=input("Enter any character:") 
if s.isalnum(): 
    print("Alpha Numeric Character") 
    if s.isalpha(): 
        print("Alphabet character") 
        if s.islower(): 
            print("Lower case alphabet character") 
        else: 
            print("Upper case alphabet character") 
    else: 
        print("it is a digit") 
elif s.isspace(): 
    print("It is space character") 
else: 
    print("Non Space Special Character")

# output
D:\python_classes>py test.py
Enter any character:7
Alpha Numeric Character
it is a digit
D:\python_classes>py test.py
Enter any character:a
Alpha Numeric Character
Alphabet character
Lower case alphabet character
D:\python_classes>py test.py
Enter any character:$
Non Space Special Character
D:\python_classes>py test.py
Enter any character:A
Alpha Numeric Character
Alphabet character
Upper case alphabet character

```
