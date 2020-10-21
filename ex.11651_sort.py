"""
Date : 10/21/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/11651
Description : sorting by second element
"""

case = int(input())
coor = []

for i in range(case):
    coor.append(list(map(int, input().split())))

coor.sort(key = lambda x: (x[1], x[0]))
print(coor)

for i in range(case):
    for j in range(0, case-i-1):
        if coor[j][1] > coor[j+1][1]:
            temp = coor[j]
            coor[j] = coor[j+1]
            coor[j+1] = temp

for item in coor:
    print(item[0], item[1])

