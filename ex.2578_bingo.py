"""
Date : 10/19/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/43165
Description : dfs / bfs
"""

bingo = []

for i in range(5):
    num = input()
    num_lit = num.split()
    bingo.append(list(map(int, num_lit)))
    

print(bingo)


