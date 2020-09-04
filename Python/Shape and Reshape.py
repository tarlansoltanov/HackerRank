# Name : Shape and Reshape
# Link : https://www.hackerrank.com/challenges/np-shape-reshape/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = input().split()

arr = numpy.array(arr, int)

print(arr.reshape(3, 3))
