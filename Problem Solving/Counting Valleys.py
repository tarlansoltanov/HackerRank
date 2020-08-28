# Name : Counting Valleys
# Link : https://www.hackerrank.com/challenges/counting-valleys/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def countingValleys(n, s):
    ans = 0
    level = 0
    for i in s:
        if i == "D":
            if level == 0:
                ans += 1
            level -= 1
        if i == "U":
            level += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
