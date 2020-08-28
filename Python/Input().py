# Name : Input()
# Link : https://www.hackerrank.com/challenges/input/problem
# Difficulty : Easy
# Programming language : Python

x, k = map(int, input().split())

s = input()

s.replace("x", str(x))

print(eval(s) == k)
