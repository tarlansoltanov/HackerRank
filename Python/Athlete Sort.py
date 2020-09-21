# Name : Athlete Sort
# Link : https://www.hackerrank.com/challenges/python-sort-sort/problem
# Difficulty : Medium
# Programming language : Python

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    ans = sorted(arr, key=lambda x: x[k])

    for i in range(len(ans)):
        p = ' '.join(str(j) for j in ans[i])
        print(p)
