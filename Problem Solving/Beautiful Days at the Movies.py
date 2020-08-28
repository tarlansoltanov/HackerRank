# Name : Beautiful Days at the Movies
# Link : https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def beautifulDays(i, j, k):
    ans = 0
    for i in range(i, j+1):
        m = ''.join(reversed(list(str(i))))
        n = abs(i - int(m))
        if(n % k == 0):
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
