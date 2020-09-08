# Name : Floor, Ceil and Rint
# Link : https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
# Difficulty : Easy
# Programming language : Python

import numpy

arr = numpy.array(list(map(float, input().split())))

numpy.set_printoptions(sign=' ')

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
