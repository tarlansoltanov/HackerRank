# Name : Cut the sticks
# Link : https://www.hackerrank.com/challenges/cut-the-sticks/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    ans = []
    while len(arr) != 0:
        ans.append(len(arr))
        x = min(arr)
        i = 0
        while i < len(arr):
            arr[i] -= x
            if arr[i] == 0:
                del arr[i]
                i -= 1
            i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
