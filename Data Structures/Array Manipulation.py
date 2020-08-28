# Name : Array Manipulation
# Link : https://www.hackerrank.com/challenges/crush/problem
# Difficulty : Hard
# Programming language : Python

import math
import os
import random
import re
import sys


def arrayManipulation(n, queries):
    ans = [0 for i in range(1, n+3)]

    maxx = 0

    x = 0

    for i in range(0, len(queries)):
        ans[int(queries[i][0])] += queries[i][2]

        ans[int(queries[i][1])+1] -= queries[i][2]

    for i in ans:
        x += i

        maxx = max(maxx, x)

    return maxx


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
