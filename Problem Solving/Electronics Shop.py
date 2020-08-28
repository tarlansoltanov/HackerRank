# Name : Electronics Shop
# Link : https://www.hackerrank.com/challenges/electronics-shop/problem
# Difficulty : Easy
# Programming language : Python

import os
import sys
from itertools import product


def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        return -1
    s = list(product(keyboards, drives))
    ans = 0
    for i in s:
        if sum(i) <= b:
            ans = max(ans, sum(i))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
