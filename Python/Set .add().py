# Name : Set .add()
# Link : https://www.hackerrank.com/challenges/py-set-add/problem
# Difficulty : Easy
# Programming language : Python

n = int(input())

countries = set()

for _ in range(n):
    countries.add(input())

print(len(countries))
