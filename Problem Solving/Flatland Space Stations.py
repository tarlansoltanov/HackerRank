# Name : Flatland Space Stations
# Link : https://www.hackerrank.com/challenges/flatland-space-stations/problem
# Difficulty : Easy
# Programming language : Python


import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    c = sorted(c)
    ans = []
    k = 0
    for i in range(n):
        if k < len(c) and i == c[k]:
            ans.append(0)
            k += 1
        elif k < len(c):
            ans.append(min(abs(i-c[k]), abs(i-c[k-1])))
        else:
            ans.append(abs(i-c[k-1]))
    return max(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
