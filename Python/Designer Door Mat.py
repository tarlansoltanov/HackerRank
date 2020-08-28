# Name : Designer Door Mat
# Link : https://www.hackerrank.com/challenges/designer-door-mat/problem
# Difficulty : Easy
# Programming language : Python

n, m = map(int, input().split())

pat = ".|."

count = (n-1)//2

for i in range(1, count+1):
    print((pat*(i*2-1)).center(m, "-"))
print("WELCOME".center(m, "-"))
while count >= 1:
    print((pat*(count*2-1)).center(m, "-"))
    count -= 1
