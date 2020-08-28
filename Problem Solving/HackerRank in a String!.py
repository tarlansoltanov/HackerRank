# Name : HackerRank in a String!
# Link : https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys
import re


def hackerrankInString(s):
    if re.search('.*?'.join(list("hackerrank")), s):
        return "YES"
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
