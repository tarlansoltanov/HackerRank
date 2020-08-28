# Name : Bon Appétit
# Link : https://www.hackerrank.com/challenges/bon-appetit/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    if (sum(bill)-bill[k])/2 == b:
        print("Bon Appetit")
    else:
        print(abs(int((sum(bill)-bill[k])/2-b)))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
