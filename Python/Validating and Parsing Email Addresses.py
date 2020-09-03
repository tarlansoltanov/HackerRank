# Name : Validating and Parsing Email Addresses
# Link : https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Difficulty : Easy
# Programming language : Python

import email.utils
import re

x = re.compile(r'^[A-Za-z]([A-Za-z0-9-_.]+)\@([A-Za-z]+)\.([A-Za-z]{1,3})$')

for _ in range(int(input())):
    person = email.utils.parseaddr(input())
    if x.match(person[1]):
        print(email.utils.formataddr(person))
