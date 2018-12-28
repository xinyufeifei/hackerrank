#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    keyboards = list(reversed(sorted(keyboards)))
    drivers = sorted(drives)
    spend_amount = 0
    i = 0
    j = 0
    while i < len(keyboards):
        while j < len(drivers):
            a = keyboards[i] + drivers[j]
            if a > b:
                break
            else:
                if a > spend_amount:
                    spend_amount = a  
                j += 1
        i += 1

    if spend_amount == 0:
        return -1
    else:
        return spend_amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
