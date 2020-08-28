# Name : Capitalize!
# Link : https://www.hackerrank.com/challenges/capitalize/problem
# Difficulty : Easy
# Programming language : Python

def solve(s):
    return ' '.join(i.capitalize() for i in s.split(" "))
