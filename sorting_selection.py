#Also uses nested loops, therefore, not fast.
#Small data sets agan <= 10000
#O(n^2) run time.

import time
import random

def selection_sort(A):
    for i in range (0, len(A) - 1):
        minIndex = i
        for j in range (i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]

def main():

    arr = [random.randint(1,10) for _ in range(10000)]
    arr3 = [33, 23, 13, 99, 3333]

    t0 = time.time()
    selection_sort(arr)
    t1 = time.time()

    total = t1-t0
    print("Time it took selection_sort: " + str(total))

    selection_sort(arr3)
    print ("Sorted array is:")
    for i in range(len(arr3)):
        print ("%d" %arr3[i])

main()
