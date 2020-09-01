# Name : The Love-Letter Mystery
# Link : https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def theLoveLetterMystery(s):
    ans = 0
    for i in range(len(s)//2):
        ans += abs(ord(s[len(s)-1-i])-ord(s[i]))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
