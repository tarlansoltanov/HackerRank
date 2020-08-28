# Name : Print Function
# Link : https://www.hackerrank.com/challenges/python-print/problem
# Difficulty : Easy
# Programming language : Python

def ans(n):
    ans = 0
    k = 10
    for i in range(1, n+1):
        if i == k:
            k *= 10
        ans = ans*k+i
    return ans


if __name__ == '__main__':
    n = int(input())
    print(ans(n))
