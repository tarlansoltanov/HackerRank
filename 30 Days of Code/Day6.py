# Name : Day 6: Let's Review
# Link : https://www.hackerrank.com/challenges/30-review-loop/problem
# Difficulty : Easy
# Programming Language : Python

def edr(s):
    even = [s[i] for i in range(0, len(s), 2)]
    odd = [s[i] for i in range(1, len(s), 2)]
    even = ''.join(j for j in even)
    odd = ''.join(j for j in odd)
    return even + " " + odd


n = int(input())
for i in range(0, n):
    s = input()
    print(edr(s))
