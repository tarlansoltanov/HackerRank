# Name : Validating phone numbers
# Link : https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# Difficulty : Easy
# Programming language : Python

import re

x = re.compile(r'^[7|8|9]([0-9]{9})$')

for _ in range(int(input())):
    print("YES" if x.match(input()) != None else "NO")
