# Name : Standardize Mobile Number Using Decorators
# Link : https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# Difficulty : Easy
# Programming language : Python

def wrapper(f):
    def fun(l):
        ans = []
        for x in l:
            if len(x) == 10:
                ans.append(f'+91 {x[:5]} {x[5:]}')
            elif len(x) == 11 and x[0] == '0':
                ans.append(f'+91 {x[1:6]} {x[6:]}')
            elif len(x) == 12 and x[0:2] == '91':
                ans.append(f'+91 {x[2:7]} {x[7:]}')
            elif len(x) == 13 and x[0:3] == '+91':
                ans.append(f'+91 {x[3:8]} {x[8:]}')
        return f(ans)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
