# Name : Polynomials
# Link : https://www.hackerrank.com/challenges/np-polynomials/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = numpy.array(list(map(float, input().split())))
print(numpy.polyval(arr, int(input())))
