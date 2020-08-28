# Name : Kangaroo
# Link : https://www.hackerrank.com/challenges/kangaroo/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if (v1-v2) == 0:
        return "NO"
    k = (x2-x1)/(v1-v2)
    if k < 0 or k.is_integer() == False:
        return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
