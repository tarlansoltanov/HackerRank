# Name : Time Conversion
# Link : https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty : Easy
# Programming language : Python

import os
import sys


def timeConversion(s):
    s = '00' + s[2:] if s[0:2] == '12' else s
    return s[:8] if s[8] == 'A' else str(int(s[0:2])+12) + s[2:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
