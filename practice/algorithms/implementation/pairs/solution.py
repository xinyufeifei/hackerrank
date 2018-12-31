#!/bin/python3

import math
import os
import random
import re
import sys
#from collections import defaultdict

# Complete the pairs function below.
def pairs(k, arr):
    i = 0
    j = 1
    count = 0
    sorted_arr = sorted(arr)
    while j < len(sorted_arr):
        diff = sorted_arr[j] - sorted_arr[i]
        if diff  == k:
            count += 1
            i += 1
            j += 1
        elif diff > k:
            i += 1
        else:
            j += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

