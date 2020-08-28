# Name : itertools.product()
# Link : https://www.hackerrank.com/challenges/itertools-product/problem
# Difficulty : Easy
# Programming language : Python

from itertools import product

a = map(int, input().split())
b = map(int, input().split())

print(' '.join(str(i) for i in product(a, b)))
