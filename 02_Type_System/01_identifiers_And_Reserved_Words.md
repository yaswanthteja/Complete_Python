# Identifiers

- A name in Python program is called identifier.
- It can be `class name` or `function name` or `module name` or `variable name`.

Example:

```
a = 10
```

## Rules to define identifiers in Python:

1. The only allowed characters in Python are

   - alphabet symbols(either lower case or upper case)
   - digits(0 to 9)
   - underscore symbol(_)
     By mistake if we are using any other symbol like $ then we will get syntax error.

     Example:

     - cash = 10 √
     - ca$h =20 (not valid)
2. Identifier should not starts with digit

   - 123total (not valid should not start with Digits )
   - total123 √
3. Identifiers are case sensitive. Of course Python language is case sensitive language.

   - total=10
   - TOTAL=999
   - print(total) #10
   - print(TOTAL) #999

## Identifier:

1. Alphabet Symbols (Either Upper case OR Lower case)
2. If Identifier is start with Underscore (_) then it indicates it is private.
3. Identifier should not start with Digits.
4. Identifiers are case sensitive.
5. We cannot use reserved words as identifiers
   Eg: def=10 
6. There is no length limit for Python identifiers. But not recommended to use too lengthy
   identifiers.
7. Dollor ($) Symbol is not allowed in Python.

Q. Which of the following are valid Python identifiers?

1) 123total (not valid because identifiers should not start with Digits)
2) total123 √
3) java2share √
4) ca$h (not valid because of special character $)
5) _abc_abc_ √
6) def (not valid because it is reserved word)
7) if (not valid because it is reserved word)

*Note:*

1. If identifier starts with _ symbol then it indicates that it is private
2. If identifier starts with __(two under score symbols) indicating that strongly private identifier.
3. If the identifier starts and ends with two underscore symbols then the identifier is
   language defined special name,which is also known as magic methods.

Eg: `__add__`

# Reserved words

In Python some words are reserved to represent some meaning or functionality. Such type of words are called Reserved words.

There are 35reserved words available in Python.

- True,False,None
- and, or ,not,is
- if,elif,else
- while,for,break,continue,return,in,yield
- try,except,finally,raise,assert
- import,from,as,class,def,pass,global,nonlocal,lambda,del,with

`Note:`

1. All Reserved words in Python contain only alphabet symbols.
2. Except the following 3 reserved words, all contain only lower case alphabet symbols.
   - True
   - False
   - None

Eg:
 a= true (not valid ,it is a reserved word)
 a=True √ (valid, True is not reserved word)

Just open your terminal and type python or python3 and run the following

```
>>> import keyword
>>> keyword.kwlist
```

Output

```
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


```

Now we are gonna see some outlines of the variable and functions. which is required to start our first program.
later we gonna study indepth about these topics in the comming topics

# Variables

variables are names which are used to store data.
Here names can be anything but it should follow the identifier rules for naming a variable.

Examples

- variable=10
- a=10
- b=20

# Functions

If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately.

We have to define these statements as a single unit and we can call that unit any number of times based on our requirement without rewriting. This unit is nothing but function.

The main advantage of functions is code Reusability.

Note: In other languages functions are known as methods,procedures,subroutines etc.

### Python supports 2 types of functions


1. Built in Functions

   Examples:

   - print()
   - input()
   - eval()
   - id()
   - type()
2. User Defined Functions

syntax:

```
  def function_name(parameters) :
 """ doc string"""
 ----
 -----
 return value

```
