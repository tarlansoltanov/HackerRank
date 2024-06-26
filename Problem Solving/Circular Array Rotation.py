# Name : Circular Array Rotation
# Link : https://www.hackerrank.com/challenges/circular-array-rotation/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def circularArrayRotation(a, k, queries):
    ans = []
    for i in range(k):
        m = a.pop()
        a.insert(0, m)
    print(a)
    for i in queries:
        ans.append(a[i])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
