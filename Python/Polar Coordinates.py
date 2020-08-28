# Name : Polar Coordinates
# Link : https://www.hackerrank.com/challenges/polar-coordinates/problem
# Difficulty : Easy
# Programming language : Python

import cmath

n = complex(input())

print(abs(n))

print(cmath.phase(n))
