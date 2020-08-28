# Name : Symmetric Difference
# Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
# Difficulty : Easy
# Programming language : Python

M = int(input())
a = set(map(int, input().split(" ")))

N = int(input())
b = set(map(int, input().split(" ")))

ans = sorted(a.symmetric_difference(b))

for i in ans:
    print(i)
