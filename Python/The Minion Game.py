# Name : The Minion Game
# Link : https://www.hackerrank.com/challenges/the-minion-game/problem
# Difficulty : Medium
# Programming language : Python

def minion_game(s):
    st_count = 0
    kv_count = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if s[i] not in vowel:
            st_count += len(s)-i
        elif s[i] in vowel:
            kv_count += len(s)-i
    if st_count > (kv_count+1):
        print("Stuart", st_count)
    elif st_count < (kv_count):
        print("Kevin", kv_count)
    else:
        print("Draw")
