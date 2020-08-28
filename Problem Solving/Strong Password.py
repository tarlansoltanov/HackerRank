# Name : Strong Password
# Link : https://www.hackerrank.com/challenges/strong-password/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    check = {'n': False, 'l': False, 'u': False, 's': False}
    ans = 4
    for i in password:
        if 'n' == True and 'l' == True and 'u' == True and 's' == True:
            break
        elif check['n'] == False and i in list(numbers):
            check['n'] = True
            ans -= 1
        elif check['l'] == False and i in list(lower_case):
            check['l'] = True
            ans -= 1
        elif check['u'] == False and i in list(upper_case):
            check['u'] = True
            ans -= 1
        elif check['s'] == False and i in list(special_characters):
            check['s'] = True
            ans -= 1
    return (ans if n+(ans) >= 6 else 6-n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
