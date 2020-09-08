# Name : Game of Thrones - I
# Link : https://www.hackerrank.com/challenges/game-of-thrones/problem
# Difficulty : Easy
# Programming language : Python

from collections import Counter
import math
import os
import random
import re
import sys


def gameOfThrones(s):
    k = 0
    myDict = Counter(s)
    arr = list(myDict.values())
    for i in arr:
        if i % 2 == 1:
            if k == 0:
                k += 1
                continue
            return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
