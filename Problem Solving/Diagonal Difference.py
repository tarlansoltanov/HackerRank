# Name : Diagonal Difference
# Link : https://www.hackerrank.com/challenges/diagonal-difference/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    n = 0
    m = 0
    for i in range(len(arr)):
        n += arr[i][i]
        m += arr[len(arr)-1-i][i]
    return abs(n-m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
