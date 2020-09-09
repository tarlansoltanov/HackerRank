# Name : Sherlock and Squares
# Link : https://www.hackerrank.com/challenges/sherlock-and-squares/problem
# Difficulty : Easy
# Programming language : Python


import math
import os
import random
import re
import sys


def squares(a, b):
    ans = 0
    while int(a**0.5)*int(a**0.5) != a:
        if a == b:
            return ans
        a += 1
    ans += 1
    while a+(int(a**0.5)*2+1) <= b:
        ans += 1
        a += (int(a**0.5)*2+1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
