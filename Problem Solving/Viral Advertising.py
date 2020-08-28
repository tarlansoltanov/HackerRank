# Name : Viral Advertising
# Link : https://www.hackerrank.com/challenges/strange-advertising/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    ans = 0
    count = 5
    for i in range(n):
        ans += count//2
        count = count//2*3
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
