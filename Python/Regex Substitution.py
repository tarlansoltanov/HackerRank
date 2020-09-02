# Name : Regex Substitution
# Link : https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Difficulty : Medium
# Programming language : Python

import re


def replace(match):
    if match.group(0) == "&&":
        return "and"
    if match.group(0) == "||":
        return "or"


for _ in range(int(input())):
    print(re.sub(r'(?<= )(\&\&)(?= )|(?<= )(\|\|)(?= )', replace, input()))
