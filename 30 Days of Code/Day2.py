# Name : Day 2: Operators
# Link : https://www.hackerrank.com/challenges/30-operators/problem
# Difficulty : Easy
# Programming Language : Python

import math
import os
import random
import re
import sys


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    ans = meal_cost + tip + tax
    return round(ans)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    print(solve(meal_cost, tip_percent, tax_percent))
