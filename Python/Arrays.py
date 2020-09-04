# Name : Arrays
# Link : https://www.hackerrank.com/challenges/np-arrays/problem
# Difficulty : Easy
# Programming language : Python

import numpy


def arrays(arr):
    result = numpy.array(list(reversed(arr)), float)
    return result


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
