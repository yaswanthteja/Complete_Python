### 1. Find the Sum of List Elements:

Write a Python function to find the sum of all elements in a given list.

```python
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Sum of list elements:", sum_of_list(my_list))
```

```python
Sum of list elements: 15
```

1. We define a function called **`sum_of_list`** that takes one parameter **`lst`**, representing the input list whose elements we want to sum.
2. **Initialization:**
Inside the function, we initialize a variable named **`total`** to store the sum of elements. We set its initial value to 0.
3. **Iterating through the List:**
We use a for loop to iterate through each element **`num`** in the input list **`lst**.
4. **Adding Elements to Total:**
Within the loop, we add each element **`num`** to the **`total`** variable.
5. **Returning the Total Sum:**
After iterating through all elements in the list, we return the final value of the **`total`** variable, which represents the sum of all elements in the list.
6. **Example Usage:**
Finally, we demonstrate how to use the function by creating a sample list **`my_list`** containing integers **`[1, 2, 3, 4, 5]`**. We then call the **`sum_of_list`** function with **`my_list`** as an argument and print the result.

```python
# sum of list elements
def sum_of_list(lst):
    return sum(lst)

my_list = [1, 2, 3, 4, 5]
print("Sum of list elements:", sum_of_list(my_list))
```

```python
Sum of list elements: 15
```

### 2.Count Occurrences of an Element:

Write a Python function to count the number of occurrences of a specific element in a given list.

```python
def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count

# Example usage:
my_list = [1, 2, 2, 3, 2, 4, 5, 2]
target_element = 2
print("Occurrences of", target_element, "is", count_occurrences(my_list, target_element))
```

```python
Occurrences of 2 is 4
```

1. **Function Definition:**
We define a function called **`count_occurrences`** that takes two parameters:
    - **`lst`**: The input list where we want to count occurrences.
    - **`target`**: The specific element whose occurrences we want to count.
2. **Initialization:**
Inside the function, we initialize a variable named **`count`** to store the count of occurrences. We set its initial value to 0.
3. **Iterating through the List:**
We use a for loop to iterate through each element **`item`** in the input list **`lst`**.
4. **Counting Occurrences:**
Within the loop, we check if the current element **`item`** is equal to the **`target`** element. If they are equal, we increment the **`count`** variable.
5. **Returning the Count:**
After iterating through all elements in the list, we return the final value of the **`count`** variable, which represents the number of occurrences of the **`target`** element in the list.
6. **Example Usage:**
Finally, we demonstrate how to use the function by creating a sample list **`my_list`** and specifying the **`target_element`** whose occurrences we want to count. We call the **`count_occurrences`** function with **`my_list`** and **`target_element`** as arguments and print the result.

### count the no of elements in list

```python
def count_lst(lst):
	count=0
	for i in lst:
		count+=1
	return count

print("Count of elements is",count_lst(lst))
```

### 3. Reverse a List:

Write a Python function to reverse the elements of a given list.

```python
def reverse_list(lst):
    return lst[::-1]

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(my_list))
```

```python
Reversed list: [5, 4, 3, 2, 1]
```

1. **Function Definition:**
We define a function called **`reverse_list`** that takes one parameter **`lst`**, which represents the input list whose elements we want to reverse.
2. **List Slicing:**
Inside the function, we use list slicing with a step of -1 (**`lst[::-1]`**) to reverse the elements of the input list.
3. **Returning the Reversed List:**
After reversing the elements, we return the reversed list.
4. **Example Usage:**
Finally, we demonstrate how to use the function by creating a sample list **`my_list`**. We then call the **`reverse_list`** function with **`my_list`** as an argument and print the reversed list.

### 4. Check Palindrome List:

Write a Python function to check if a given list is a palindrome or not (i.e., if it reads the same forwards and backwards).

```python
def is_palindrome(lst):
    return lst == lst[::-1]

# Example usage:
my_list1 = [1, 2, 3, 2, 1]
my_list2 = [1, 2, 3, 4, 5]
print("Palindrome:", is_palindrome(my_list1))
print("Palindrome:", is_palindrome(my_list2))
```

```python
Palindrome: True
Palindrome: False
```

1. **Function Definition:**
We define a function called **`is_palindrome`** that takes one parameter **`lst`**, which represents the input list that we want to check for palindrome.
2. **List Slicing:**
Inside the function, we use list slicing with a step of -1 (**`lst[::-1]`**) to reverse the elements of the input list.
3. **Comparison:**
We then compare the original list **`lst`** with its reversed version (**`lst[::-1]`**) to check if they are equal.
4. **Returning the Result:**
If the original list and its reversed version are equal, then the list is a palindrome, and we return **`True`**. Otherwise, we return **`False`**.
5. **Example Usage:**
Finally, we demonstrate how to use the function by creating two sample lists **`my_list1`** and **`my_list2`**. We then call the **`is_palindrome`** function with each list as an argument and print the result.

### 5. Remove Duplicates from List:

Write a Python function to remove duplicate elements from a given list while preserving the original order of elements.

```python
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

# Example usage:
my_list = [1, 2, 2, 3, 4, 4, 5, 5]
print("List with duplicates removed:", remove_duplicates(my_list))
```

```python
List with duplicates removed: [1, 2, 3, 4, 5]
```

1. **Function Definition:**
We define a function called **`remove_duplicates`** that takes one parameter **`lst`**, which represents the input list from which we want to remove duplicate elements.
2. **Initialization:**
Inside the function, we initialize an empty set **`seen`** to keep track of unique elements that we have encountered so far. We also initialize an empty list **`result`** to store the unique elements in the order of their first occurrence.
3. **Iterating through the List:**
We use a for loop to iterate through each element **`item`** in the input list **`lst`**.
4. **Removing Duplicates:**
Within the loop, for each element **`item`**, we check if it is not already in the set **`seen`**. If it is not, we append it to the **`result`** list and add it to the **`seen`** set to mark it as seen.
5. **Returning the Result:**
After iterating through all elements in the list, we return the final value of the **`result`** list, which contains only the unique elements in the original order.
6. **Example Usage:**
Finally, we demonstrate how to use the function by creating a sample list **`my_list`** containing duplicate elements. We then call the **`remove_duplicates`** function with **`my_list`** as an argument and print the result.

### 7. Average of list

```python
# Average of list

def average_of_list(lst):
    return sum(lst) / len(lst)

my_list = [1, 2, 3, 4, 5]
print("Average of list elements:", average_of_list(my_list))
```

```python
Average of list elements: 3.0
```

1. **Function Definition:**
    - The function **`average_of_list`** takes one parameter **`lst`**, which represents the input list.
2. **Calculation:**
    - Inside the function, **`sum(lst)`** calculates the sum of all elements in the list **`lst`**.
    - **`len(lst)`** calculates the number of elements in the list.
    - Dividing the sum of elements by the number of elements gives us the average.
3. **Return Value:**
    - The function returns the calculated average.
4. **Example Usage:**
    - A sample list **`my_list`** is defined with elements **`[1, 2, 3, 4, 5]`**.
    - The **`average_of_list`** function is called with **`my_list`** as an argument.
    - The average of the elements in the list is printed.
    
    ### 8. Maximum  elements of list
    
    ```python
    # Maximum elements of list
    
    def max_of_list(lst):
        return max(lst)
    
    my_list = [1, 2, 3, 4, 5]
    print("Maximum element in list:", max_of_list(my_list))
    ```
    
    ```python
    Maximum element in list: 5
    ```
    
    1. **Function Definition:**
        - The function **`min_of_list`** takes one parameter **`lst`**, which represents the input list.
    2. **Calculation:**
        - Inside the function, **`min(lst)`** returns the minimum element in the list **`lst`**.
    3. **Return Value:**
        - The function returns the minimum element found in the list.
    4. **Example Usage:**
        - A sample list **`my_list`** is defined with elements **`[1, 2, 3, 4, 5]`**.
        - The **`min_of_list`** function is called with **`my_list`** as an argument.
        - The minimum element in the list is printed.
        
        ### 9. Minimum Elements of list
        
        ```python
        def min_of_list(lst):
            return min(lst)
        
        my_list = [1, 2, 3, 4, 5]
        print("Minimum element in list:", min_of_list(my_list))
        
        ```
        
        ```python
        Minimum element in list: 1
        ```
        
        1. **Function Definition:**
            - The function **`min_of_list`** takes one parameter **`lst`**, which represents the input list.
        2. **Calculation:**
            - Inside the function, **`min(lst)`** returns the minimum element in the list **`lst`**.
        3. **Return Value:**
            - The function returns the minimum element found in the list.
        4. **Example Usage:**
            - A sample list **`my_list`** is defined with elements **`[1, 2, 3, 4, 5]`**.
            - The **`min_of_list`** function is called with **`my_list`** as an argument.
            - The minimum element in the list is printed.
            
            ### 10. Merge Two Sorted Lists:
            
            Write a Python function to merge two sorted lists into a single sorted list.
            
            ```
            def merge_sorted_lists(list1, list2):
                merged_list = []
                i, j = 0, 0
                while i < len(list1) and j < len(list2):
                    if list1[i] < list2[j]:
                        merged_list.append(list1[i])
                        i += 1
                    else:
                        merged_list.append(list2[j])
                        j += 1
                merged_list.extend(list1[i:])
                merged_list.extend(list2[j:])
                return merged_list
            
            # Example usage:
            list1 = [1, 3, 5, 7, 9]
            list2 = [2, 4, 6, 8, 10]
            print("Merged sorted list:", merge_sorted_lists(list1, list2))
            ```
            
            ```python
            Merged sorted list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            ```
            
            1. **Function Definition:**
                - The function **`merge_sorted_lists`** takes two parameters **`list1`** and **`list2`**, which represent the two sorted lists to be merged.
            2. **Initialization:**
                - Inside the function, we initialize an empty list **`merged_list`** to store the merged sorted list.
                - We also initialize two pointers **`i`** and **`j`** to keep track of the current position in each list.
            3. **Merging Process:**
                - We use a while loop to iterate through both lists simultaneously until either list is exhausted.
                - During each iteration, we compare the elements at the current positions of **`list1`** and **`list2`**.
                - We append the smaller element to the **`merged_list`** and increment the corresponding pointer (**`i`** or **`j`**).
            4. **Remaining Elements:**
                - After the loop, there may be remaining elements in either **`list1`** or **`list2`**.
                - We extend the **`merged_list`** with the remaining elements from both lists.
            5. **Return Value:**
                - Finally, we return the **`merged_list`**, which contains all elements from both input lists in sorted order.
            6. **Example Usage:**
                - Sample lists **`list1`** and **`list2`** are defined with elements **`[1, 3, 5, 7, 9]`** and **`[2, 4, 6, 8, 10]`**, respectively.
                - The **`merge_sorted_lists`** function is called with **`list1`** and **`list2`** as arguments.
                - The merged sorted list is printed.
                
                ### 11. Find Maximum and Minimum Element:
                
                Write a Python function to find the maximum and minimum elements in a given list.
                
                ```python
                def find_max_min(lst):
                    if not lst:
                        return None, None  # Return None for both max and min if list is empty
                    max_element = min_element = lst[0]  # Initialize max_element and min_element with the first element of the list
                    for num in lst:
                        if num > max_element:
                            max_element = num  # Update max_element if current element is greater
                        elif num < min_element:
                            min_element = num  # Update min_element if current element is smaller
                    return max_element, min_element
                
                # Example usage:
                my_list = [5, 3, 9, 1, 7]
                max_num, min_num = find_max_min(my_list)
                print("Maximum element:", max_num)
                print("Minimum element:", min_num)
                ```
                
                ```python
                Maximum element: 9
                Minimum element: 1
                ```
                
                1. **Function Definition:**
                    - The function **`find_max_min`** takes one parameter **`lst`**, which represents the input list.
                2. **Initialization:**
                    - We initialize **`max_element`** and **`min_element`** with the first element of the list (**`lst[0]`**).
                3. **Iterating through the List:**
                    - We use a for loop to iterate through each element **`num`** in the list **`lst`**.
                    - For each element, we compare it with the current **`max_element`** and **`min_element`** and update them accordingly.
                4. **Returning the Result:**
                    - After iterating through all elements, we return the final values of **`max_element`** and **`min_element`**.
                5. **Example Usage:**
                    - A sample list **`my_list`** is defined with elements **`[5, 3, 9, 1, 7]`**.
                    - The **`find_max_min`** function is called with **`my_list`** as an argument.
                    - The maximum and minimum elements found in the list are printed.
                    
                    ### 12. Rotate List by K Positions:
                    
                    Write a Python function to rotate the elements of a given list to the right by K positions.
                    
                    ```python
                    def rotate_list(lst, k):
                        n = len(lst)
                        # If the list is empty or k is zero, return the original list
                        if not lst or k % n == 0:
                            return lst
                        k = k % n  # Adjust k to be within the range of list length
                        return lst[-k:] + lst[:-k]
                    
                    # Example usage:
                    my_list = [1, 2, 3, 4, 5]
                    k = 2
                    rotated_list = rotate_list(my_list, k)
                    print("Original list:", my_list)
                    print("Rotated list by", k, "positions:", rotated_list)
                    ```
                    
                    ```python
                    Original list: [1, 2, 3, 4, 5]
                    Rotated list by 2 positions: [4, 5, 1, 2, 3]
                    ```
                    
                    1. **Function Definition:**
                        - The function **`rotate_list`** takes two parameters: **`lst`**, representing the input list, and **`k`**, representing the number of positions to rotate the list to the right.
                    2. **Length of the List:**
                        - We calculate the length of the list **`n`** using **`len(lst)`**.
                    3. **Edge Cases Handling:**
                        - If the list is empty or **`k`** is zero, we return the original list as there is no need to rotate.
                        - If **`k`** is a multiple of **`n`** (i.e., rotating by a full cycle), we return the original list.
                    4. **Adjusting K:**
                        - We adjust **`k`** to be within the range of list length by taking the modulus **`%`** of **`k`** with **`n`**.
                    5. **Rotating the List:**
                        - We split the list into two parts: the last **`k`** elements and the first **`n-k`** elements.
                        - Then, we concatenate these two parts in reverse order to rotate the list to the right by **`k`** positions.
                    6. **Example Usage:**
                        - A sample list **`my_list`** is defined with elements **`[1, 2, 3, 4, 5]`**.
                        - We specify **`k = 2`** to rotate the list by 2 positions to the right.
                        - The **`rotate_list`** function is called with **`my_list`** and **`k`** as arguments.
                        - The original list and the rotated list are printed for comparison.
                        
                    
                    ```python
                    def rotate_list(nums, k):
                        k = k % len(nums)
                        return nums[-k:] + nums[:-k]
                    
                    nums = [1, 2, 3, 4, 5]
                    k = 2
                    print("Rotated list:", rotate_list(nums, k))
                    ```
                    
                    ```python
                    Rotated list: [4, 5, 1, 2, 3]
                    ```
                    
                    ### 13.  Find Missing Number:
                    
                    Write a Python function to find the missing number in a list containing consecutive integers from 1 to N (where N is the length of the list).
                    
                    ```python
                    def find_missing_number(nums):
                        n = len(nums) + 1  # Length of the list is N - 1, so adding 1 to get N
                        expected_sum = n * (n + 1) // 2  # Sum of consecutive integers from 1 to N
                        actual_sum = sum(nums)  # Sum of elements in the list
                        return expected_sum - actual_sum
                    
                    # Example usage:
                    my_list = [1, 2, 3, 5, 6, 7, 8]
                    missing_number = find_missing_number(my_list)
                    print("Missing number in the list:", missing_number)
                    ```
                    
                    ```python
                    Missing number in the list: 4
                    ```
                    
                    1. **Function Definition:**
                        - The function **`find_missing_number`** takes one parameter **`nums`**, which represents the list containing consecutive integers from 1 to N (with one number missing).
                    2. **Length of the List:**
                        - We calculate the length of the list **`n`** as **`len(nums) + 1`**. Adding 1 is necessary because one number is missing in the list.
                    3. **Expected Sum:**
                        - We calculate the expected sum of consecutive integers from 1 to N using the formula **`n * (n + 1) // 2`**.
                    4. **Actual Sum:**
                        - We calculate the actual sum of elements in the list using the **`sum()`** function.
                    5. **Missing Number Calculation:**
                        - The missing number is obtained by subtracting the actual sum from the expected sum.
                    6. **Example Usage:**
                        - A sample list **`my_list`** is defined with elements **`[1, 2, 3, 5, 6, 7, 8]`**. Here, the missing number is 4.
                        - The **`find_missing_number`** function is called with **`my_list`** as an argument.
                        - The missing number in the list is printed.
                        
                        ### 14.  Check for Sub list:
                        
                        Write a Python function to check if a given list is a sublist of another list.
                        
                        ```python
                        def is_sublist(sublist, lst):
                            n, m = len(lst), len(sublist)
                            for i in range(n - m + 1):
                                if lst[i:i + m] == sublist:
                                    return True
                            return False
                        
                        # Example usage:
                        main_list = [1, 2, 3, 4, 5, 6, 7]
                        sub_list = [3, 4, 5]
                        print("Is sub_list a sublist of main_list?", is_sublist(sub_list, main_list))
                        ```
                        
                        ```python
                        Is sub_list a sublist of main_list? True
                        ```
                        
                        1. **Function Definition:**
                            - The function **`is_sublist`** takes two parameters: **`sublist`**, representing the sublist to be checked, and **`lst`**, representing the main list.
                        2. **Lengths of Lists:**
                            - We obtain the lengths of both lists: **`n`** for the main list and **`m`** for the sublist.
                        3. **Iterating through the Main List:**
                            - We use a for loop to iterate through the main list **`lst`**.
                            - For each starting index **`i`** in the main list where a sublist could potentially start (**`n - m + 1`**), we compare the sublist starting from index **`i`** with the given sublist.
                            - If a match is found, we return **`True`** immediately.
                        4. **Returning False:**
                            - If no match is found after iterating through all possible starting indices, we return **`False`**.
                        5. **Example Usage:**
                            - Sample lists **`main_list`** and **`sub_list`** are defined.
                            - The **`is_sublist`** function is called with **`sub_list`** and **`main_list`** as arguments.
                            - The result of whether **`sub_list`** is a sublist of **`main_list`** is printed.
                        
                    
                    ## 15. Write a program that prompts user to specify the length of a list and then requests numbers to populate that list. Display the final list as the output.
                    
                    ```python
                    list_length=int(input("Enter the length: "))
                    result=[]
                    for i in range(list_length):
                    	num=int(input(f"Enter the value at position {i} = "))
                    	result.append(num)
                    print(result)
                    ```
                    
                    ```python
                    Enter the length: 3
                    Enter the value at position 0 = 10
                    Enter the value at position 1 = 25
                    Enter the value at position 2 = 564
                    [10, 25, 564]
                    ```
                    
                    ### 16. Replace element in list
                    
                    ```python
                    def replace(lst,old,new):
                    	for i in range(len(lst)):
                    		if lst[i]==old:
                    			lst[i]=new
                    	return lst
                    
                    lst=[52,25,5,10,5,8,6,5]
                    old=int(input("Enter the replacing element: "))
                    new=int(input("Enter the new element: "))
                    print(replace(lst,old,new))
                    ```
                    
                    ```python
                    Enter the replacing element: 5
                    Enter the new element: 2
                    [52, 25, 2, 10, 2, 8, 6, 2]
                    ```
                    
                    ### 17. Remove all even elements from the list
                    
                    ```python
                    
                    lst=[5,6,3,8,9,12,2]
                    od_lst=[]
                    for i in range(len(lst)):
                    	if lst[i]%2!=0:
                    		od_lst.append(lst[i])
                    print(od_lst) 
                    ```
                    
                    ```python
                    [5, 3, 9]
                    ```
                    
                    ### 18. Remove the elements which are not divisible by the number entered by the user
                    
                    ```python
                    
                    def remove_divisible(lst, divisor):
                        return [x for x in lst if x % divisor != 0]
                    
                    # Example usage
                    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    divisor = 3
                    result = remove_divisible(numbers, divisor)
                    print("Original List:", numbers)
                    print("Divisor:", divisor)
                    print("List after removing elements divisible by", divisor, ":", result)
                    
                    ```
                    
                    ```python
                    Original List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    Divisor: 3
                    List after removing elements divisible by 3 : [1, 2, 4, 5, 7, 8, 10]
                    ```
                    
                    ```python
                    def remove_divisible(lst, divisor):
                        result = []
                        for i in lst:
                            if i % divisor != 0:
                                result.append(i)
                        return result
                    
                    # Example usage
                    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    divisor = 3
                    result = remove_divisible(numbers, divisor)
                    print("Original List:", numbers)
                    print("Divisor:", divisor)
                    print("List after removing elements divisible by", divisor, ":", result)
                    
                    ```
                    
                    ### 19. Take a list and pull out odd and even numbers from the list.
                    
                    ```python
                    lst=[1,25,65,46,99,3,4,5]
                    odd=[]
                    even=[]
                    for i in lst:
                    	if i%2==0:
                    		even.append(i)
                    	else:
                    		odd.append(i)
                    print("odd list: ",odd)
                    print("even list: ",even)
                    
                    ```
                    
                    ```python
                    odd list:  [1, 25, 65, 99, 3, 5]
                    even list:  [46, 4]
                    ```
                    
                    ### 20. Create a program that merges elements of two lists into a single list.
                    
                    ```python
                    lst1=[1,2,3,4,5]
                    lst2=[6,7,8,9,10]
                    lst3=[]
                    for i in lst1:
                    	lst3.append(i)
                    for j in lst2:
                    	lst3.append(j)
                    print(lst3)
                    ```
                    
                    ```python
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    ```
                    
                    ```python
                    lst1=[1,2,3,4,5]
                    lst2=[6,7,8,9,10]
                    lst3=lst1+lst2
                    print(lst3)
                    ```
                    
                    ```python
                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                    ```

		     ### 21. write a program that has two lists and make a new list that contains only the common elements between them without duplicates.

```python
lst1=[1,2,3,4,5]
lst2=[3,4,5,6,7]
lst3=[]
for i in lst1:
		if i in lst2:
			lst3.append(i)
print(lst3)
```

```python
[3, 4, 5]
```

### 22. write a program to find second largest num in the list

```python
lst=[1,2,3,4,5]

largest=0
second_largest=0
for num in lst:
	if num>largest:
		second_largest=largest
		largest=num
	elif num> second_largest and num< largest:
		second_largest=num
print(second_largest)
```

```python
4
```

### 23 . write a program that takes a list of integers and returns the product of all the elements.

```python
my_list=[1,2,3,4,5]
product=1

for num in my_list:
	product=product*num
print(product)
 
```

```python
120
```

## 24. write a program to find and print all prime numbers with in a given list.

```python
my_list=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for num in my_list:
	factors=0
	for i in range(1,num+1):
		if num%i==0:
			factors+=1
	if factors==2:
		print(num)
```

```python
2
3
5
7
11
13
```

### 25. write a program to split a given list into two halves.

```python
def split_list(lst):
    mid = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    return first_half, second_half

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
first_half, second_half = split_list(my_list)
print("First half:", first_half)
print("Second half:", second_half)

```

```python
First half: [1, 2, 3, 4]
Second half: [5, 6, 7, 8]
```

### 26. write a program to swap the first and last elements of a given list.

```python
def swap_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

my_list = [1, 2, 3, 4, 5]
swapped_list = swap_first_last(my_list)
print("List after swapping first and last elements:", swapped_list)

```

```python
List after swapping first and last elements: [5, 2, 3, 4, 1]
```

