#Not the fastest because of the use of the nested loopsself.
#Useful only will small data sets. (<= 10000)
#Runs in O(n^2)

import time
import random

def insertion_sort(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

#Optimized: shifting to swapping
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum

def main():
    # arr = [12, 11, 13, 5, 6]
    # arr2 = [14, 13, 11, 7, 9]
    # arr3 = [33, 23, 13, 99, 3333]

    arr = [random.randint(1,10) for _ in range(10000)]
    arr2 = [random.randint(1,10) for _ in range(10000)]
    arr3 = [random.randint(1,10) for _ in range(10000)]

    t0 = time.time()
    insertion_sort(arr)
    t1 = time.time()

    total = t1-t0

    # print ("Sorted array is:")
    print("Time it took insertion_sort: " + str(total))
    # for i in range(len(arr)):
    #     print ("%d" %arr[i])


    t2 = time.time()
    insertion_sort2(arr2)
    t3 = time.time()

    total_2 = t3-t2

    # print ("Sorted array is:")
    print("Time it took insertion_sort2: " + str(total))
    # for i in range(len(arr2)):
    #     print ("%d" %arr2[i])

    t4 = time.time()
    insertion_sort3(arr3)
    t5 = time.time()

    total_3 = t5-t4

    # print ("Sorted array is:")
    print("Time it took insertion_sort3: " + str(total))
    # for i in range(len(arr3)):
    #     print ("%d" %arr3[i])

main()
