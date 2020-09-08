# Name : Inner and Outer
# Link : https://www.hackerrank.com/challenges/np-inner-and-outer/problem
# Difficulty : Easy
# Programming language : Python

import numpy

numpy.set_printoptions(legacy='1.13')

arr1 = numpy.array(list(map(int, input().split())))

arr2 = numpy.array(list(map(int, input().split())))

print(numpy.inner(arr1, arr2))

print(numpy.outer(arr1, arr2))
