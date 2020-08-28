# Name : Simple Array Sum
# Link : https://www.hackerrank.com/challenges/simple-array-sum/problem
# Difficulty : Easy
# Programming language : Python

import os
import sys


def simpleArraySum(ar):
    ans = 0
    for i in ar:
        ans += i
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
