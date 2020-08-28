# Name : Alphabet Rangoli
# Link : hackerrank.com/challenges/alphabet-rangoli/problem
# Difficulty : Easy
# Programming language : Python

import string


def print_rangoli(n):
    alpha = string.ascii_lowercase
    ans = []
    size = n+(n-1)*3
    for i in range(n):
        m = '-'.join(alpha[i:n])
        ans.append((m[::-1]+m[1:]).center(size, '-'))
    ans = list(reversed(ans))+ans[1:]
    print('\n'.join(ans))
