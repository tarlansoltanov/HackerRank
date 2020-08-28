# Name : List Comprehensions
# Link : https://www.hackerrank.com/challenges/list-comprehensions/problem
# Difficulty : Easy
# Programming language : Python

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x_list = [e for e in range(x+1)]
    y_list = [e for e in range(y+1)]
    z_list = [e for e in range(z+1)]
    ans = [[a,b,c]  for a in x_list for b in y_list for c in z_list if a+b+c!=n]
    print(ans)
    
