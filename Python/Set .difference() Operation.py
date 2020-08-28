# Name : Set .difference() Operation
# Link : https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
print(len(a - b))
