# Name : Grading Students
# Link : https://www.hackerrank.com/challenges/grading/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] < 38:
            continue
        elif grades[i] % 5 > 2:
            grades[i] = (grades[i]//5+1)*5
    return grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
