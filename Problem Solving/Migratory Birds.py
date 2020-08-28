# Name : Migratory Birds
# Link : https://www.hackerrank.com/challenges/migratory-birds/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    sarr = set(arr)
    count = 0
    num = 0
    for i in sarr:
        if arr.count(i) > count:
            num = i
            count = arr.count(i)
    return num


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
