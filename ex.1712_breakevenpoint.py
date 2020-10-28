'''
Date : 10/28/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/1712
Description : break-even point
'''

a,b,c = map(int, input().split())


if b >= c :
    print(-1)
else :
    print(a//(c-b) + 1)
