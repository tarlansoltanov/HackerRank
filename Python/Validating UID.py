# Name : Validating UID
# Link : https://www.hackerrank.com/challenges/validating-uid/copy-from/177613319
# Difficulty : Easy
# Programming language : Python

import re

x = re.compile(
    r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$')

for _ in range(int(input())):
    s = input()
    if x.match(s) != None:
        print("Valid")
    else:
        print("Invalid")
