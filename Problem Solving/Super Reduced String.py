# Name : Super Reduced String
# Link : https://www.hackerrank.com/challenges/reduced-string/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

def superReducedString(s):
    s = list(s)
    i = 0
    while i<len(s)-2:
        if len(s)==0:
            return "Empty String"
        if s[i]==s[i+1]:
            del s[i]
            del s[i]
            i=0
            continue
        i+=1
    if s[len(s)-2]==s[len(s)-1]:
        del s[len(s)-1]
        del s[len(s)-1]
    if len(s)==0:
        return "Empty String"
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()

