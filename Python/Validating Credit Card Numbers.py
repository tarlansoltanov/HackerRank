# Name : Validating Credit Card Numbers
# Link : https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# Difficulty : Medium
# Programming language : Python

import re

x = re.compile(r'(?!.*(\d)(-?\1){3})')

k = re.compile(
    r'^[456]([0-9]{3})([-])?([0-9]{4})([-])?([0-9]{4})([-])?([0-9]{4})$')

for _ in range(int(input())):
    s = input()
    if x.match(s) != None and k.match(s) != None:
        print("Valid")
    else:
        print("Invalid")
