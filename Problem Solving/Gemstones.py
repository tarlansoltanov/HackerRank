# Name : Gemstones
# Link : https://www.hackerrank.com/challenges/gem-stones/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def gemstones(arr):
    ans = set(arr[0])
    for i in arr:
        ans = ans & set(i)
    return len(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
