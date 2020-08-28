# Name : Apple and Orange
# Link : https://www.hackerrank.com/challenges/apple-and-orange/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    ans1 = 0

    ans2 = 0

    for i in range(0, len(apples)):
        if(apples[i]+a >= s and apples[i]+a <= t):
            ans1 += 1

    for i in range(0, len(oranges)):
        if(oranges[i]+b >= s and oranges[i]+b <= t):
            ans2 += 1
    print(ans1, ans2, sep='\n')


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
