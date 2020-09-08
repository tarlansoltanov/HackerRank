# Name : Eye and Identity
# Link : https://www.hackerrank.com/challenges/np-eye-and-identity/problem
# Difficulty : Easy
# Programming language : Python

import numpy

n, m = map(int, input().split())

numpy.set_printoptions(sign=' ')

print(numpy.eye(n, m, k=0))
