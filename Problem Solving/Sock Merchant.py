# Name : Sock Merchant
# Link : https://www.hackerrank.com/challenges/sock-merchant/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    sar = set(ar)
    ans = 0
    for i in sar:
        ans += (ar.count(i)//2)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
