# Name : Text Wrap
# Link : https://www.hackerrank.com/challenges/text-wrap/problem
# Difficulty : Easy
# Programming language : Python

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))
