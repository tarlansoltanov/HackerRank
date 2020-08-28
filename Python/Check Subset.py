# Name : Check Subset
# Link : https://www.hackerrank.com/challenges/py-check-subset/problem
# Difficulty : Easy
# Programming language : Python

for _ in range(int(input())):
    m = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    print(a & b == a)
