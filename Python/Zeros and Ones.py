# Name : Zeros and Ones
# Link : https://www.hackerrank.com/challenges/np-zeros-and-ones/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = list(map(int, input().split()))

print(numpy.zeros((arr), dtype=numpy.int))

print(numpy.ones((arr), dtype=numpy.int))
