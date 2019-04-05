# Python's built in sorting algoright, which is a mixture of merge and quick
# It is called Tim sort
# Duplicate values slows it down, but not by much

# Implemented in C

import time
import random

def main():
    arr = [random.randint(1, 1000) for _ in range(1000000)]
    arr3 = [33, 23, 13, 99, 3333]

    t0 = time.time()
    arr.sort()
    t1 = time.time()

    total = t1-t0
    print("Time it took merge_sort: " + str(total))

    print ("Sorted array is:")
    arr3.sort()
    for i in range(len(arr3)):
        print ("%d" %arr3[i])

main()
