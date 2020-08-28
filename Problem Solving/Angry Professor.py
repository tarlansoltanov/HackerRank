# Name : Angry Professor
# Link : https://www.hackerrank.com/challenges/angry-professor/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    ans = 0
    for i in a:
        if i <= 0:
            ans += 1
    return "YES" if ans < k else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
