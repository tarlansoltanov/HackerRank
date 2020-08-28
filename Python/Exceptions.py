# Name : Exceptions
# Link : https://www.hackerrank.com/challenges/exceptions/problem
# Difficulty : Easy
# Programming language : Python

num = int(input())

for i in range(0, num):
    a, b = input().split(" ")
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
