# Name : Climbing the Leaderboard
# Link : https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Difficulty : Medium
# Programming language : Python


import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    ans = []
    ranked = sorted(set(ranked))
    i = 0
    place = len(ranked)+1
    for j in player:
        while i < len(ranked) and ranked[i] <= j:
            i += 1
        ans.append(place-i)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
