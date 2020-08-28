# Name : Mars Exploration
# Link : https://www.hackerrank.com/challenges/mars-exploration/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def marsExploration(s):
    ans = 0
    x = 'SOS'*(len(s)//3)
    for i in range(len(s)):
        if x[i] != s[i]:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
