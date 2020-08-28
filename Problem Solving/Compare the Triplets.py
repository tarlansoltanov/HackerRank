# Name : Compare the Triplets
# Link : https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def compareTriplets(a, b):
    aa = 0
    bb = 0
    for i in range(len(a)):
        aa += a[i] > b[i]
        bb += b[i] > a[i]
    return [aa, bb]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
