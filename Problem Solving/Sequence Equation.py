# Name : Sequence Equation
# Link : https://www.hackerrank.com/challenges/permutation-equation/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def permutationEquation(p):
    ans = []
    for i in range(1, len(p)+1):
        m = p.index(p.index(i)+1)+1
        ans.append(m)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
