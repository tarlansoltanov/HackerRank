# Name : Between Two Sets
# Link : https://www.hackerrank.com/challenges/between-two-sets/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def check(k, arr, x=False):
    if x == 0:
        for i in arr:
            if k % i != 0:
                return False
        return True
    for i in arr:
        if i % k != 0:
            return False
    return True


def getTotalX(a, b):
    arr = set()
    minn = max(a)
    maxx = min(b)
    for i in b:
        for j in range(1, int(i**0.5)+2):
            if i % j == 0:
                if j >= minn and j <= maxx:
                    arr.add(j)
                if i//j >= minn and i//j <= maxx:
                    arr.add(i//j)
    brr = set()
    for i in arr:
        if check(i, a):
            brr.add(i)
    ans = set()
    for i in brr:
        if check(i, b, 1):
            ans.add(i)
    return len(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
