# Name : Day 11: 2D Arrays
# Link : https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Difficulty : Easy
# Programming Language : Python

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
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(arr))
