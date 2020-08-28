# Name : Day 8: Dictionaries and Maps
# Link : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Difficulty : Easy
# Programming Language : Python

n = int(input())

book = dict()

for i in range(n):
    name, phone = map(str, input().split())
    book[name] = phone
m = input()
while True:
    try:
        print(m + '=' + book[m])
    except KeyError:
        print("Not found")
    try:
        m = input()
    except EOFError:
        break
