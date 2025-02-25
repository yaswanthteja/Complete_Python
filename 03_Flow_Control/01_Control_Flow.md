## Flow  Control  


Flow control describes the order in which statements will be executed at runtime.


![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/4abfef70-d824-42f6-ad1f-ac8154422ee7)



# Conditional Statements
In Python, condition statements act depending on whether a given condition is true or false. You can execute different blocks of codes depending on the outcome of a condition. Condition statements always evaluate to either True or False.
There are three types of conditional statements.

1. if statement
2. if-else
3. if-elif-else
4. nested if-else


## 1.  if

- In control statements, The if statement is the simplest form. It takes a condition and evaluates to either True or False.

- If the condition is True, then the True block of code will be executed, and if the condition is False, then the block of code is skipped, and The controller moves to the next line.

```
if condition : statement
 or
if condition :
 statement-1
 statement-2
 statement-3
 ```
If condition is true then statements will be executed

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/6155aeec-9d80-4083-b80a-7fdb0ec60fa4)


Example:

```
number = 6
if number > 5:
    # Calculate square
    print(number * number)
print('Next lines of code')

Output

36
Next lines of code

```


## 2. If – else statement

- The if-else statement checks the condition and executes the if block of code when the condition is True, and if the condition is False, it will execute the else block of code.

Syntax of the if-else statement
```
if condition:
    statement 1
else:
    statement 2
```


- If the condition is True, then statement 1 will be executed If the condition is False, statement 2 will be executed. See the following flowchart for more detail.

![image](https://github.com/yaswanthteja/100Days_of_Python/assets/93423367/db0b22dc-361e-46be-868f-a02b02ed71d0)


```
password = input('Enter password ')

if password == "name@#29":
    print("Correct password")
else:
    print("Incorrect Password")

output -1

Enter password name@#29
Correct password

Output -2
Enter password name
Incorrect Password
```
<br/>

## 3. Chain multiple if statement in Python
In Python, the if-elif-else condition statement has an elif blocks to chain multiple conditions one after another. This is useful when you need to check multiple conditions.

With the help of if-elif-else we can make a tricky decision. The elif statement checks multiple conditions one by one and if the condition fulfills, then executes that code.

Syntax of the if-elif-else statement:
```
if condition-1:  
     statement 1 
elif condition-2:
     stetement 2 
elif condition-3:
     stetement 3 
     ...         
else:            
     statement  
 ```
Example
```
def user_check(choice):
    if choice == 1:
        print("Admin")
    elif choice == 2:
        print("Editor")
    elif choice == 3:
        print("Guest")
    else:
        print("Wrong entry")

user_check(1)
user_check(2)
user_check(3)
user_check(4)
 
Output:

Admin
Editor
Guest
Wrong entry
```

<br/>

## 4. Nested if-else statement
In Python, the nested if-else statement is an if statement inside another if-else statement. It is allowed in Python to put any number of if statements in another if statement.

Indentation is the only way to differentiate the level of nesting. The nested if-else is useful when we want to make a series of decisions.

Syntax of the nested-if-else:
```
if conditon_outer:
    if condition_inner:
        statement of inner if
    else:
        statement of inner else:
    statement ot outer if
else:
    Outer else 
statement outside if block

```
Example: Find a greater number between two numbers

```
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is greater than', num2)
else:
    print(num1, 'is smaller than', num2)
    
    
    
Output
 
Enter first number 56
Enter second number 15
56 is greater than 15

```
<br/>

## Iterative Statements

If we want to execute a group of statements multiple times then we should go for 
Iterative statements.
Python supports 2 types of iterative statements.
1. for loop
2. while loop

## 1. for loop:

- If we want to execute some action for every element present in some sequence(it may be string or collection)then we should go for for loop.
Syntax:
```
for x in sequence :
 body
 ```
- where sequence can be string or any collection.
Body will be executed for every element present in the sequence

### Example: To print characters present in the given string



```
s="performance" 
for x in s : 
  print(x) 


Output: 
p
e
r
f
o
r
m
a
n
c
e
```

<br/>


## 2. while loop:

If we want to execute a group of statements iteratively until some condition false,then we should go for while loop.
## Syntax:
```
 while condition :
 body
 ```
 
 Eg: To print numbers from 1 to 10 by using while loop
 ```

 x=1 
 while x <=10: 
    print(x) 
    x=x+1 
 ```

Eg: To display the sum of first n numbers
```
 n=int(input("Enter number:")) 
 sum=0 
 i=1 
 while i<=n: 
    sum=sum+i 
    i=i+1 
 print("The sum of first",n,"numbers is :",sum)
 ```

## Infinite Loops:

```
 i=0; 
 while True : 
 i=i+1; 
 print("Hello",i) 
```

<br/>

## 3. Transfer statements

1. break
2. continue
3. pass


## break

We can use break statement inside loops to break loop execution based on some condition.

```
for i in range(10): 
    if i==7: 
        print("processing is enough..plz break") 
        break 
    print(i) 

D:\Python_classes>py test.py 
 0 
 1 
 2 
 3 
 4 
 5 
 6 
 processing is enough..plz break 

```

<br/>

## 2. continue:
We can use continue statement to skip current iteration and continue next iteration.

Eg 1: To print odd numbers in the range 0 to 9
```
for i in range(10): 
    if i%2==0: 
        continue 
    print(i) 

D:\Python_classes>py test.py 
1 
3 
5 
7 
9 
```
<br/>

## pass statement:
pass is a keyword in Python.
In our programming syntactically if block is required which won't do anything then we can define that empty block with pass keyword.

pass
 |- It is an empty statement
 |- It is null statement
 |- It won't do anything
Eg:

if True:
SyntaxError: unexpected EOF while parsing

if True: pass
==>valid

def m1():
SyntaxError: unexpected EOF while parsing



### use case of pass:
Sometimes in the parent class we have to declare a function with empty body and child 
class responsible to provide proper implementation. Such type of empty body we can 
define by using pass keyword. (It is something like abstract method in java)


Eg:
```
for i in range(100): 
    if i%9==0: 
        print(i) 
    else:pass 

D:\Python_classes>py test.py 
0 
9 
18 
 27 
 36 
 45 
 54 
 63 
 72 
 81 
 90 
 99

```

<br/>