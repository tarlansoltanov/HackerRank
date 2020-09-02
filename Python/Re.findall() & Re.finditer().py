# Name : Re.findall() & Re.finditer()
# Link : https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Difficulty : Easy
# Programming language : Python

import re

x = re.compile(
    r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([AEIOUaeiou]{2,})(?:[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])')

k = input()

print("\n".join(x.findall(k)) if x.findall(k) else -1)
