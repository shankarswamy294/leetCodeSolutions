#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    i, count = 0, 0
    count = 0
    while i < len(arr):
        if arr[i] != i+1:
            val = arr[i]-1
            arr[i], arr[val] = arr[val], arr[i]
            count += 1
        else:
            i += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
