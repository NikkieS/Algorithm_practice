"""
Date : 11/06/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/11720
Description : sum of numbers
"""

# My Answer
l = int(input())
num = input()
ans = 0

for i in range(l):
    ans += int(num[i])

print(ans)


# Short Coding
input()

print(sum(map(int,input())))
