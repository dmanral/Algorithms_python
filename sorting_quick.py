# Recursive
# Another divide-and-conqure
# Also efficient with large data sets

# Run time
    # Worst case O(n^2), therefore, comparable to selection, insertion, etc.
    # Average case O(n log n)
    # Performance depends largly on what pivot value is selected

# With duplicates it fails because of stack overflow

import time
import random

def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)
    return A

def quick_sort2(A, low, hi):
	if hi-low < 20 and low < hi: #threshhold can change
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)

def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi

def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)

def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]

def main():
    arr = [random.randint(1, 1000) for _ in range(1000)]
    arr3 = [33, 23, 13, 99, 3333]

    t0 = time.time()
    quick_sort(arr)
    t1 = time.time()

    total = t1-t0
    print("Time it took merge_sort: " + str(total))

    print ("Sorted array is:")
    print(quick_sort(arr3))

main()
