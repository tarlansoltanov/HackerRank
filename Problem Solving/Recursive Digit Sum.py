# Name : Recursive Digit Sum
# Link : https://www.hackerrank.com/challenges/recursive-digit-sum/problem
# Difficulty : Medium
# Programming language : Python

import math
import os
import random
import re
import sys


def superDigit(n, k):
    return int(n)*k % 9 or 9


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
