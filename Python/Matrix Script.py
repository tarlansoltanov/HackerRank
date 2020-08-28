# Name : Matrix Script
# Link : https://www.hackerrank.com/challenges/matrix-script/problem
# Difficulty : Hard
# Programming language : Python

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

str = ""

for i in range(m):
    for j in range(n):
        str += matrix[j][i]

print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', " ", str))
