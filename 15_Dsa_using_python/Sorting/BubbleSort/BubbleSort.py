
# Bubble sort

def BubbleSort(Cuslist):
    # Loop through each element in the list, except the last one
    for i in range(len(Cuslist)-1):
        # Loop through the list up to the already sorted portion
        for j in range(len(Cuslist)-i-1):
            # If the current element is greater than the next element, swap them
            if Cuslist[j] > Cuslist[j+1]:
                Cuslist[j], Cuslist[j+1] = Cuslist[j+1], Cuslist[j]
    # Print the sorted list
    print(Cuslist)

# Example list to be sorted
custlist = [2, 4, 8, 9, 1, 5]
# Call the BubbleSort function with the example list
BubbleSort(custlist)
