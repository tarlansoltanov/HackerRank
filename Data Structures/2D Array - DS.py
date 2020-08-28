# Name : 2D Array - DS
# Link : https://www.hackerrank.com/challenges/2d-array/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    ans = -63
    for i in range(0, 4):
        for j in range(0, 4):
            k = 0
            k += arr[i][j]+arr[i][j+1]+arr[i][j+2]
            k += arr[i+1][j+1]
            k += arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            ans = max(ans, k)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
