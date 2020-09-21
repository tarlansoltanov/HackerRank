# Name : Manasa and Stones
# Link : https://www.hackerrank.com/challenges/manasa-and-stones/problem
# Difficulty : Easy
# Programming language : Python


import math
import os
import random
import re
import sys
from itertools import combinations_with_replacement


def stones(n, a, b):
    k = n-1
    ans = set()
    for i in combinations_with_replacement([a, b], k):
        ans.add(sum(i))
    return sorted(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
