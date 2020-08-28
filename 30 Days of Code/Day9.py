# Name : Day 9: Recursion 3
# Link : https://www.hackerrank.com/challenges/30-recursion/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys

# Complete the factorial function below.


def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return factorial(n-1)*n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
