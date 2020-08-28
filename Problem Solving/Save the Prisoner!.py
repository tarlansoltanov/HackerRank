# Name : Save the Prisoner!
# Link : https://www.hackerrank.com/challenges/save-the-prisoner/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def saveThePrisoner(n, m, s):
    ans = ((s-1)+(m-1)) % n
    return ans+1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
