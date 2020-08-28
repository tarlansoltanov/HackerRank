# Name : Mutations
# Link : https://www.hackerrank.com/challenges/python-mutations/problem
# Difficulty : Easy
# Programming language : Python

def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return ''.join(string)
