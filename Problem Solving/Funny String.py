# Name : Funny String
# Link : https://www.hackerrank.com/challenges/funny-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def funnyString(s):
    for i in range(len(s)-1):
        if abs(ord(s[i+1])-ord(s[i])) != abs(ord(s[len(s)-i-1])-ord(s[len(s)-i-2])):
            return "Not Funny"
    return "Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
