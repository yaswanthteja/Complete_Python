## Introduction

- Python is a general purpose high level programming language.
- Python was developed by Guido Van Rossam in 1989 while working at National Research Institute at Netherlands.
- But officially Python was made available to public in 1991. The official Date of Birth for Python is : Feb 20th 1991.
- Python is recommended as first programming language for beginners.

## History of Python

History of Python starts in the late 1980s at `Centrum Wiskunde` and `Informatica`, Python language was Designed by Guido Van Rossum and was first released in 1991. Python language is the successor of ABC Language which had the feature of exception handling. Guido Van Rossum worked on the creation of ABC and so he took the syntax and features of the language, then solved all the issues with the language and created a good scripting language.

## Python Language Fundamentals

**Example 1: To print Helloworld:**

## Java:

```
public class HelloWorld 
{ 
   public static void main(String[] args) 
   { 
     System.out.println("Hello world"); 
   } 
} 

```

## **`C language:`**

```

 #include<stdio.h> 
 void main() 
 { 
   print("Hello world"); 
 } 

```

## **`Python `:**

```
print("Hello World")

```



The name Python was selected from the TV Show
"**The Complete Monty Python's Circus**", which was broadcasted in BBC from 1969 to 1974.
Guido developed Python language by taking almost all programming features from
different languages

1. **Functional Programming Features from C**
2. **Object Oriented Programming Features from C++**
3. **Scripting Language Features from Perl and Shell Script**
4. **Modular Programming Features from Modula-3
   Most of syntax in Python Derived from C and ABC languages.**

## Where we can use Python:

We can use everywhere. The most common important application areas are

1. For developing Desktop Applications
2. For developing web Applications
3. For developing database Applications
4. For Network Programming
5. For developing games
6. For Data Analysis Applications
7. For Machine Learning
8. For developing Artificial Intelligence Applications
9. For IOT
   ...

### Note:

Internally Google and Youtube use Python coding
NASA and Nework Stock Exchange Applications developed by Python.
Top Software companies like Google, Microsoft, IBM, Yahoo using Python.

### Features of Python:

1. `Simple and easy to learn`:

   - Python is a simple programming language. When we read Python program,we can feel like
     reading english statements.
   - The syntaxes are very simple and only 30+ kerywords are available.When compared with other languages, we can write programs with very less number of
     lines.
   - Hence more readability and simplicity.We can reduce development and cost of the project.
2. `Freeware and Open Source`:

   - We can use Python software without any licence and it is freeware.
     Its source code is open,so that we can we can customize based on our requirement.
   - Eg: Jython is customized version of Python to work with Java Applications.
3. `High Level Programming language`:

   - Python is high level programming language and hence it is programmer friendly language.
     Being a programmer we are not required to concentrate low level activities like memory
     management and security etc..
4. `Platform Independent`:

   - Once we write a Python program,it can run on any platform without rewriting once again.
     Internally PVM is responsible to convert into machine understandable form.
5. `Portability`:

   - Python programs are portable. ie we can migrate from one platform to another platform
     very easily. Python programs will provide same results on any platform.
6. `Dynamically Typed`:

   - In Python we are not required to declare type for variables. Whenever we are assigning
     the value, based on value, type will be allocated automatically.Hence Python is considered
     as dynamically typed language.
   - But Java, C etc are Statically Typed Languages b'z we have to provide type at the beginning
     only.
     This dynamic typing nature will provide more flexibility to the programmer.
7. `Both Procedure Oriented and Object Oriented`:

   - Python language supports both Procedure oriented (like C, pascal etc) and object oriented
     (like C++,Java) features. Hence we can get benefits of both like security and reusability etc
8. `Interpreted` :

   - We are not required to compile Python programs explcitly. Internally Python interpreter
     will take care that compilation.
   - If compilation fails interpreter raised syntax errors. Once compilation success then PVM(Python Virtual Machine) is responsible to execute.
9. `Extensible`:

   - We can use other language programs in Python.
     The main advantages of this approach are:

   1. We can use already existing legacy non-Python code
   2. We can improve performance of the application.
10. `Embedded`:

    - We can use Python programs in any other language programs.
      i.e we can embedd Python programs anywhere.
11. `Extensive Library`:

    - Python has a rich inbuilt library.
    - Being a programmer we can use this library directly and we are not responsible to
      implement the functionality.
      etc..

## Limitations of Python:

1. Performance wise not up to the mark b'z it is interpreted language.
2. Not using for mobile Applications.

# Flavors of Python:

## 1. `CPython`:

- It is the standard flavor of Python. It can be used to work with C lanugage Applications.
- The prefix “C ” denotes C programing language.
  This is a compiled programing language that converts the python code to the bytecode by compiling it, and then give the code to the interpreter.
- CPython was introduced in 1994 by Python community sponsored by Python Software Foundation.
- It is faster than the original python programing language because it is a compiled language.
- It is used as the Scientific and numeric calculations and also for creating python standard modules. CPython follows the coding rules and syntax of python programing language versions 2.x.

### What is Cython ?

Cython is the standard python software implementation in programming language C. Cython is both interpreted and compiled language, that is, before it is interpreted, it compiles the text into bytecode. In 1994 the first version of CPython was released by the Python developer community.

## Uses of Cython

- Scientific and Numeric computations.
- High Traffic Websites.
- Designing Python Modules.

## 2. `Jython or JPython`:

It is for Java Applications. It can run on JVM.

Jython is another implementation of python programming language. It was introduced on January 17, 2001, which written in java and python.

- Jython was designed to give support to the python programming language on the java platforms.
- Jython used most of the standard libraries of the python except for some modules written in C.
- Jython used classes of java instead of modules of the python programming language it can import and use any java class.
- Jython compiles python code to the java bytecode either on-demand or statically. The most recent release of Jython was Jython 2.7.2 on 21 March 2020 which is compatible with python 2.7.
- Jython is a java implementation of python that combines expressive power with clarity. Jython is a powerful as well as simple because it uses Python’s syntax and Java’s environment. It allows using features of Python in Java environment or to import Java classes in Python codes and hence, it  is very flexible.
- Jython is freely available for both commercial and non-commercial use

## Advantages :

- Embedded scripting – Java programmers can add the Jython libraries to their system to allow end users to write simple or complicated scripts that add functionality to the application.
- Interactive experimentation – Jython provides an interactive interpreter that can be used to interact with Java packages or with running Java applications. This allows programmers to experiment and debug any Java system using Jython.
- Rapid application development – Python programs are typically 2-10x shorter than the equivalent Java program. This translates directly to increased programmer productivity. The seamless interaction between Python and Java allows developers to freely mix the two languages both during development and in shipping products.

### Example of Jpython :

```python
#jpython Program 

from java.lang import System # Java import

print(‘Running on Java version: ‘ + System.getProperty(‘java.version’))
print(‘Unix time from Java: ‘ + str(System.currentTimeMillis()))
```

## 3. `IronPython`:

It is for C#.Net platform.

- IronPython is the implementation of python programming language which is targeting the .Net framework of Microsoft.
- The original author of the IronPython was Jim Hugunin who contributed in the initial version of the IronPython.
- The initial implementation of IronPython was released on Sept 5 2006. Then the project of IronPython was maintained by the small team at Microsoft until the launch of the version 2.7.
- The project is now maintained by the volunteers at GitHub. IronPython is written in C# also some of the code is generated by the generator written in python.
- Interface extensibility is the key advantage of IronPython.
  IronPython is an excellent addition to the .NET Framework, providing Python developers with the power of the .NET framework.
- Existing .NET developers can also use IronPython as a fast and expressive scripting language for embedding, testing, or writing a new application from scratch
- IronPython is written entirely in C#, although some of its code is automatically generated by a code genrator written in Python.
- IronPython is implemented on top of the Dynamic Runtime Language (DLR), a library running on top of the Common Language Infrastructure that provides dynamic typing and dynamic method dispatch, among other things, for dynamic languages.
- The DLR is part of the .NET Framework 4.0 and is also a part of Mono since version 2.4 from 2009. The DLR can also be used as a library on older CLI implementations.

## 4. `PyPy`:

The main advantage of PyPy is performance will be improved because JIT compiler is available inside PVM.

- PyPy is an alternative implementation of Python programming language. It is Python interpreter and a compiler toolchain which is written in RPython. -
- Although PyPy is faster than Python programing language as it used JIT[Just-in-time Compiler].
- Most of the python codes run well on this compiler except for some which are implemented in CPython.
- PyPy was first released in mid-2007 and got a stable release in 2020 as PyPy version 7.3.1.
- Meta-tracking is the technique used by PyPy which transforms an interpreter into a compiler also called as tracking just-in-time compiler. The current version of the PyPy is compatible with most operating systems such as Windows, Mac, Linux, etc.

## What is PyPy :

- PyPy is a very compliant Python interpreter, almost a drop-in replacement for CPython 2.7.10 and 3.3.5. It’s fast due to its integrated tracing JIT compiler.
- On average, PyPy is 4.2 times faster than CPython. Sometimes Cpython may get TLE  while execution but the same code may run fine with PyPy.In general if c++ takes 1 second to execute a file , if we execute same file with python it will take upto 5 seconds.

## PyPy Advantages and distinct Features:

- Speed: thanks to its Just-in-Time compiler, Python programs often run faster on PyPy.
- Memory usage: memory-hungry Python programs (several hundreds of MBs or more) might end up taking less space than they do in CPython.
- Compatibility: PyPy is highly compatible with existing python code. It supports cffi, cppyy, and can run popular python libraries like twisted, and django. It can also run NumPy, Scikit-learn and more via a c-extension compatibility layer.
- Stackless: It comes by default with support for stackless mode, providing micro-threads for massive concurrency.

## 5. `RubyPython`:

For Ruby Platforms

## 6. `AnacondaPython`:

It is specially designed for handling large volume of data processing.

# Do you  know what flavour of python is installed in your computer??

let's check that out
By defaultly we use CPython.

### How can you confirm if you are using CPython?

- To verify the Python implementation, you are using on your machine you can use the Python platform module. And specifically the python implementation() function
- The Python implementation on this machine is CPython that as I explained before is the reference implementation of Python.
- And let’s see what the output is for Python 3.
- Open your Terminal and type `python`or `python3` and run the following code.

```
 import platform
 platform.python_implementation()

 Output:
'CPython'

```

# Python Versions:

- Python 1.0V introduced in Jan 1994
- Python 2.0V introduced in October 2000
- Python 3.0V introduced in December 2008

``Note: Python 3 won't provide backward compatibility to Python2``.

i.e there is no guarantee that Python2 programs will run in Python3.

# Applications of Python

Python programming language s used in many areas of development. Due to its easy understand ability and good user interface, it is used in many scientific fields. Many heavy operations Numeric and scientific calculations, Research, and development, Scraping and many more. Some applications are:

- Machine Learning
- Artificial Intelligence
- Web Scraping
- Data Science and Analysis
- GUI
  etc.

Python has good library support that makes a programmer to write the program more easily and efficiently. It has library support for machine learning, Scraping, GUI, etc.

## Companies using Python

- Instagram
- Spotify
- Amazon
- Google
- Netflix

# Why Python ?

Python can run on different platforms like Windows, Mac, Linux, etc.

- It is easy to learn syntax as they are the same as the English language.
- Python codes are shorter than compared to other programming languages and hence are easy to write and debug.
- Python can be treated in an object-oriented, procedural, or functional way as it supports the concept of object-oriented programming and also functional programming. Some Special points in history of python are:

  - It has a wast, active and supportive community.
  - Sponsor of Python is Google.
  - Huge library support.
  - Efficient and easy to learn.
  - Python is accessible.

[The process to generate the output.]

![The process to generate the output](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/6e122ad4-826d-429f-b052-6588a851cc5d)

# What is bytecode in Python

You reffer this 04_Internal_working_of_Python.md to know in detail.

## ByteCode

Machines are not able to understand the human language or high-level languages thus whenever we write code in any programming language, machine used a compiler or an interpreter to convert the human-readable code to machine code.

When the code is converted to machine code a new file is created which is easier for a machine to understand and execute. Such files contain code in bytes which is the machine-readable format. So let’s discuss on the question more, What is bytecode in Python.

[Stages for generating output in Python]()

![Stages for generating output in Python](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/d931884d-f28d-4ca0-8341-22aed998c9e1)

- Byte codes are referred to as the portable codes or p-codes. When a python code is interpreted into the machine language then the python code gets converted into bytes.
- These bytecodes are also called as the set of instructions for the virtual machine and the python interpreter is the implementation of the virtual machine.
- The set The intermediate format is called the bytecode. Bytecodes are :
  - Lower-level
  - Platform Independent
  - Efficient
  - Intermediate
  - Representation of source code

Bytecode is the low-level representation of the python code which is the platform-independent, but the code is not the binary code and so it cannot run directly on the targeted machine.

 It is a set of instructions for the virtual machine which is also called as the Python Virtual Machine [PVM]. When the Python code is interpreted, it is converted to the compiled bytecode file referred to as the PYC file.

  Pyc files have the set of instructions to follow in sequence to generate the output. These pyc files are faster than the normal python code files

# Bytecodes in pyc files

Python programming language is an interpreter language which converts the python code to the bytecode.
These bytecodes are created by a compiler present inside the interpreter.

- Interpreter first compiles the python code t0 the byte code which is also called as the intermediate code, then the code is used to run on the virtual machine.
- In the virtual machine, the library modules of the python get added and then the code is ready to run on a machine. Steps for interpretation of python source code :

  - Source code: Python Code
  - Compiler: Enters inside the compiler to generate the bytecode
  - Bytecode: Intermediate code or low-level code
  - Virtual Machine: Here the code gets the support from the library modules.

Python is slower as compared to another programming language, but the process of converting the python code to the bytecode makes it faster to access each time after the code is interpreted once.

 This bytecode is saved in the file named same as the source file but with a different extension named as “pyc”.

This pyc files contain compiled version of the source code which makes the code more efficient to run on the virtual machine

# Difference Between .py and .pyc Files

- Files with extension .py contain Python code that is human readable. On the other side .pyc files contain bytecode that is not human readable. Files with .py extension are compiled into .pyc files that are then processed by the Python interpreter.
- Files with .py extension are Python source files, the files in which you write your Python code.
- The Python code you write in .py files is not executed in the same format by the machine on which you run your code.
- Before being executed, the code in the .py files is compiled into .pyc files.
- Imagine the compilation process as a translation from one language to another language.

The .pyc file is not fully readable because it’s a compiled version of the original .py file contains bytecode.

# _pycache_ files

All the interpreted files are stored in the _pycache_ files. We can say _pycache_ file is a folder containing all the interpreted .pyc files. The data in .pyc files in the _pycahce _ folder the is the bytecode representation of the python source code.

## Where are Compiled Files Created when Using Python 3?

 In the previous Python 2 We have seen that a .pyc file has been created in the same directory of the .py file when importing the module.

- Note: Considering that Python 2 is very old you should really be using Python 3
- In Python 3 the compiled version of the code for a given module is created in a different location compared to  Python 2.
- After importing the  module we can use the dir() built-in function to get a list of module attributes we can access.
- There’s one attribute I want you to focus on:[`` __cached__``](https://docs.python.org/3/reference/import.html#__cached__).

The [``__cached__``](https://docs.python.org/3/reference/import.html#__cached__)  attribute for a Python module is the path of the compiled version of that module. The addition of this attribute was a proposal part of [PEP 3147](https://peps.python.org/pep-3147/).

Note: PEP stands for Python Enhancement Proposals.
When using Python 3 the filename also contains the Python implementation (cpython) and the version of Python (38).

## When Do .pyc Files Get Updated?

Python recreates the .pyc file for a given module when that module is modified and reimported.

## Can You Delete .pyc Files?

You can delete .pyc files, if you do that and then you import that module again the .pyc file related to that module gets recreated. Here you can see the .pyc created before.

Another tool that aims to simplify this across all platforms is the [pyclean package](https://pypi.org/project/pyclean/). To use this package, you install it using pip, make sure you’re in the directory you want to clean, and run:  pyclean -v .

# Dynamic Typing vs Static Typing

Dynamic typing and static typing are two different attributes of programming language on which they can be divided.

 Python is a dynamically typed language which means checking of the variable is done at the runtime. Whereas in the Statically typed language the checking of the variables or any other is done at the compile time.

 Dynamically typed language is easier to write as no need to initialize the type of the variable, but it also creates confusion while the code is revisited. Let’s see more on “Dynamic Typing vs Static Typing in Python”.

## Dynamically Typed language:

A language is considered as Dynamically typed language if the variable type of the language is checked at the runtime of the code compilation or code interpretation.

 In such type of programming languages, we don’t need to initialize a variable with its type. We can declare a variable by writing the name at left and the value at the left of the variable name, Ex Var = 90. Some

dynamically typed languages are:

- Python
- PHP
- JavaScript
  As the memory allocation and variable checking are done at the runtime of the code, these type of languages are not considered as less optimised than statically typed language.

## Statically typed language

In statically typed languages the type of the variable s checked at the compile time of the variable declaration.

 Statically programming languages check the type of the variable or abject while the code enters the compiler. Unlike dynamically typed languages we need to write the type of the variable during initializing it. Ex in java, int Var = 10. Some statically typed languages are:

- Java
- C
- C++

In Statically typed languages once if a variable is initialized to a data-type it cannot be assigned to the variable of a different type. Statically typed languages are faster than dynamically typed languages.

[Dynamictyping]()

[Differences between dynamic typing and static typing]()
