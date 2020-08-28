# Name : Set .intersection() Operation
# Link : https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
print(len(a & b))
