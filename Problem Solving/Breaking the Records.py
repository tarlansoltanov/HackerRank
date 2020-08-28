# Name : Breaking the Records
# Link : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    minn_count = 0
    minn = scores[0]
    maxx_count = 0
    maxx = scores[0]
    for i in scores:
        if i < minn:
            minn_count += 1
            minn = i
        elif i > maxx:
            maxx_count += 1
            maxx = i
    return [maxx_count, minn_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
