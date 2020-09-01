# Name : Alternating Characters
# Link : https://www.hackerrank.com/challenges/alternating-characters/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    ans = 0
    last = 0
    i = 0
    while i < len(s):
        if s[i] != last:
            last = s[i]
            i += 1
        else:
            ans += 1
            i += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
