# Name : Day 25: Running Time and Complexity
# Link : https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem
# Difficulty : Medium
# Programming Language : Python

def check(n):
    if n == 1:
        return "Not prime"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Not prime"
    return "Prime"


n = int(input())

for _ in range(n):
    k = int(input())
    print(check(k))
