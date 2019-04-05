#Recursive as it calls itself.
#Divide and conqure algorithm.
#Very efficient for large data sets.

#Run time:
    #It does log n merge steps because each merge step doubles the list size
    #It does n work for each merge step because it must look at every item
    #Runs in O(n log n)

import time
import random

def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)   #List, Start index, Ending index
    return A

def merge_sort2(A, first, last):    #List, First index, Last index
    if first < last:                #If there is more than one item in the list, then we break the list
        middle = (first + last)//2  #divide with integral result (discard remainder)
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    left = A[first:middle]          #left half of list
    right = A[middle:last+1]        #right half of list
    left.append(999999999)          #so we know when we reach the end of list
    right.append(999999999)         #so we know when we reach the end of list
    i = j = 0                       #i for left and j for right set indecies to 0
    for k in range(first, last+1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


def main():
    arr = [random.randint(1,10) for _ in range(1000000)] #Million still only takes ~6 seconds
    arr3 = [33, 23, 13, 99, 3333]

    t0 = time.time()
    merge_sort(arr)
    t1 = time.time()

    total = t1-t0
    print("Time it took merge_sort: " + str(total))

    print ("Sorted array is:")
    print(merge_sort(arr3))

main()
