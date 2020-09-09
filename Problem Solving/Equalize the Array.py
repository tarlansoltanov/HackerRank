# Name : Equalize the Array
# Link : https://www.hackerrank.com/challenges/equality-in-a-array/problem
# Difficulty : Easy
# Programming language : Python

from collections import Counter
import math
import os
import random
import re
import sys


def equalizeArray(arr):
    count = Counter(arr)
    return sum(list(count.values()))-max(list(count.values()))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
