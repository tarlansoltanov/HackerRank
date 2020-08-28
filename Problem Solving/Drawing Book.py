# Name : Drawing Book
# Link : https://www.hackerrank.com/challenges/drawing-book/problem
# Difficulty : Easy
# Programming language : Python

import os
import sys


def pageCount(n, p):
    ans = min(p//2, (n-p)//2)
    if (n-p) == 1 and n % 2 == 0 and n != 2:
        ans = 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
