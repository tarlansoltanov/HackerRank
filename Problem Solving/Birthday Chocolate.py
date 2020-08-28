# Name : Birthday Chocolate
# Link : https://www.hackerrank.com/challenges/the-birthday-bar/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

from itertools import combinations


def birthday(s, d, m):
    ans = 0
    for i in range(len(s)-m+1):
        sm = 0
        for j in range(m):
            sm += s[i+j]
        if sm == d:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
