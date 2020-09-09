# Name : Minimum Distances
# Link : https://www.hackerrank.com/challenges/minimum-distances/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def minimumDistances(arr):
    ans = len(arr)+5
    for i in range(len(arr)):
        if arr[i] in arr[i+1:]:
            ans = min(ans, arr[i+1:].index(arr[i])+1)
    return ans if ans != len(arr)+5 else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
