# Name : Picking Numbers
# Link : https://www.hackerrank.com/challenges/picking-numbers/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def pickingNumbers(a):
    sa = set(a)
    ans = 0
    for i in sa:
        ans = max(a.count(i)+a.count(i+1), ans)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
