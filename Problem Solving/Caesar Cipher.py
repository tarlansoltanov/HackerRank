# Name : Caesar Cipher
# Link : https://www.hackerrank.com/challenges/caesar-cipher-1/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

from queue import deque

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet = deque(alphabet)


def rotate(k, arr):
    for i in range(k):
        x = arr.popleft()
        arr.append(x)
    return list(arr)


def check(x, k):
    if k.isupper():
        return x.upper()
    return x


def caesarCipher(s, k):
    ans = ''
    alphabet1 = list(alphabet)
    alphabet2 = rotate(k, alphabet)
    for i in s:
        if i.lower() in alphabet1:
            k = alphabet1.index(i.lower())
            ans += check(alphabet2[k], i)
        else:
            ans += i
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
