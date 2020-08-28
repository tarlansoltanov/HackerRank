# Name : Lists
# Link : https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty : Easy
# Programming language : Python

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        s = input().split()
        cmd = s[0]
        argues = s[1:]
        if cmd != "print":
            cmd += "(" + ",".join(argues) + ")"
            eval("arr."+cmd)
        else:
            print(arr)
