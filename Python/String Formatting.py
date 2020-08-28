# Name : String Formatting
# Link : https://www.hackerrank.com/challenges/python-string-formatting/problem
# Difficulty : Easy
# Programming language : Python

def print_formatted(number):
    w = len(bin(number).replace('0b', ''))
    for i in range(1, number+1):
        print('{} {} {} {}'.format(str(i).rjust(w, ' '), oct(i).replace('0o', '').rjust(w, ' '), hex(
            i).upper().replace('0X', '').rjust(w, ' '), bin(i).replace('0b', '').rjust(w, ' ')))
