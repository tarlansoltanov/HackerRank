# Name : Left Rotation
# Link : https://www.hackerrank.com/challenges/array-left-rotation/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    while d > 0:
        k = a[0]
        del a[0]
        a.append(k)
        d -= 1

    print(' '.join(str(i) for i in a))
