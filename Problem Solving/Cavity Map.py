# Name : Cavity Map
# Link : https://www.hackerrank.com/challenges/cavity-map/problem
# Difficulty : Easy
# Programming language : Python

import math
import os
import random
import re
import sys


def cavityMap(grid):
    for i in range(1, len(grid)-1):
        grid[i] = list(grid[i])
        for j in range(1, len(grid[i])-1):
            maxx = max(max(grid[i-1][j], grid[i][j-1]),
                       max(grid[i+1][j], grid[i][j+1]))
            if grid[i][j] > maxx:
                grid[i][j] = 'X'
        grid[i] = ''.join(grid[i])
    return grid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
