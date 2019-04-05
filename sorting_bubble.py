#Slow, longer than both insertion and selection.
#Small data sets <= 10000.
#O(n^2) due to nested loops.

import time
import random

def bubble_sort(A): #A is a list.
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def main():
    arr = [random.randint(1,10) for _ in range(10000)]
    arr3 = [33, 23, 13, 99, 3333]

    t0 = time.time()
    bubble_sort(arr)
    t1 = time.time()

    total = t1-t0
    print("Time it took bubble_sort: " + str(total))


    print ("Sorted array is:")
    print(bubble_sort(arr3))


main()
