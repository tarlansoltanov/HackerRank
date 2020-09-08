# Name : String Construction
# Link : https://www.hackerrank.com/challenges/string-construction/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def stringConstruction(s):
    return(len(set(s)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
