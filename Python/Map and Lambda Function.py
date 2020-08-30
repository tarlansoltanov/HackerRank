# Name : Map and Lambda Function
# Link : https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
# Difficulty : Easy
# Programming language : Python

def cube(x): return x**3


def fibonacci(n):
    ans = []
    for i in range(n):
        if i == 0 or i == 1:
            ans.append(i)
            continue
        ans.append(ans[i-1]+ans[i-2])
    return ans


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
