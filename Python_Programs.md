
# 1.Write a code to reverse a number
```
num = int(input("Enter the Number:"))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print("The Given number is {} and Reverse is {}".format(temp, reverse))
```
# 2 Write code Check if the given string is Palindrome or not
```
#take user input
String1 = input('Enter the String :')
#initialize string and save reverse of 1st string
String2 = String1[::-1]
#check if both matches
if String1 == String2:
    print('String is palindromic')
else:
    print('Strings is not palindromic')
```

# 3.Write code to check a String is palindrome or not?
```
# function which return reverse of a string

def isPalindrome(s): 
  return s == s[::-1]


# Driver code 
s = "malayalam"
ans = isPalindrome(s)

if ans: 
  print("Yes") 
else: 
  print("No")
  
```

# 4.Write code of Greatest Common Divisor 
```
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
 

def gcdFunction(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd = i
    print("GCD of two Number: {}".format(gcd))

gcdFunction(num1, num2)

```
# 5.Write code of  Perfect number
```
n = int(input("Enter any number: "))
sump= 0
for i in range(1, n):
    if(n % i == 0):
        sump= sump + i
if (sump == n):
    print(" The number is a Perfect number")
else:
    print(" The number is not a Perfect number")
```
# 6.Write a code to Remove all characters from string except alphabets
```
#take user input
String1 = input('Enter the String :')
#initialize empty String
String2 = ''
for i in String1:
    #check for alphabets
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        #concatenate to empty string
        String2+=i
print('Alphabets in string are :' + String2)
```
# 7.Write a program to check whether a character is a vowel or consonant
```
#get user input
Char =  input() 
#Check if the Char belong to set of Vowels
if (Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u'): 
    #if true 
    print("Character is Vowel") 
else: 
    #if false
    print("Character is Consonant")

```
# 8.Write a program for Binary to Decimal to conversion
```
num = int(input("Enter number:"))
binary_val = num
decimal_val = 0
base = 1
while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {} and Decimal Number is {}".format(binary_val, decimal_val))
```
   
   

## 9 Write a code to Remove all characters from string except alphabets
```
#take user input
String1 = input('Enter the String :')
#initialize empty String
String2 = ''
for i in String1:
    #check for alphabets
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        #concatenate to empty string
        String2+=i
print('Alphabets in string are :' + String2)
```

## 10  Can we reverse a list in Python?
Yes, we can reserve a list in Python using the reverse() method. The code is as follows:
```
def reverse(s):
 str = "" 
 for i in s: 
   str = i + str
  return str
  
  ```




## 11 Write a Python script to implement the Bubble sort algorithm.
Code
```
# Python program to show how to implement bubble sort  
  
def bubble_Sort(array):  
    n = len(array)  
  
for i in range(n-1):  
         
for j in range(0, n-i-1):  
             
if array[j] > array[j + 1] :  
                array[j], array[j + 1] = array[j + 1], array[j]  
     
print(array)  
  
#example array  
arr = [23, 14, 64, 13, 64, 23, 86]  
  
bubble_Sort(arr)  
```
Output:
```
[13, 14, 23, 23, 64, 64, 86]
```

## 12 In Python, create a program that generates a Fibonacci sequence.
Code
```
#taking number of terms to print the series  
n = 9  
first = 0 #first value of series  
second = 1 #second value of series  
series = [first, second]  
if n == 0:  
     
print("The required fibonacci series is",first)  
else:  
     
for i in range(0,n-2):   
         
num = series[i] + series[i+1]  
         
series.append(num)  
print(series)  
```
```
Output:

[0, 1, 1, 2, 3, 5, 8, 13, 21]
```

## 13 Remove duplicates from sorted array
Given an integer sorted array in increasing order, remove the duplicate numbers such that each unique element appears only once. Make sure you keep the final order of the array the same.

It is impossible to change the length of the array in Python, so we will place the result in the first part of the array. After removing duplicates, we will have k elements, and the first k elements in the array should hold the results. 

![image](https://user-images.githubusercontent.com/93423367/216781101-b3050608-9c0c-435d-90a6-f0945a39ce46.png)


Example 1: input array is [1,1,2,2], the function should return 2. 

Example 2: input array is [1,1,2,3,3], the function should return 3.

Solution:

- Run the loop for the range of 1 to the size of the array.
- Check if the previous number is unique or not. We are comparing previous elements with the current one.  
- If it is unique, update the array using insertIndex, which is 1 at the start, and add +1 to the insertIndex. 
- Return insertIndex as it is the k. 
- This question is relatively straightforward once you know how. If you put more time into understanding the statement, you can easily come up with a solution.


```
def removeDuplicates(array):
    size = len(array)
    insertIndex = 1
    for i in range(1, size):
        if array[i - 1] != array[i]:
            # Updating insertIndex in our main array
            array[insertIndex] = array[i]
            # Incrementing insertIndex count by 1
            insertIndex = insertIndex + 1
    return insertIndex

array_1 = [1,2,2,3,3,4]
removeDuplicates(array_1)
# 4


array_2 = [1,1,3,4,5,6,6]
removeDuplicates(array_2)
# 5
```
