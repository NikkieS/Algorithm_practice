'''
Date : 10/22/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2675
Description : string format loop
'''
case = int(input())

T = []

for i in range(case):
    
    T.append(input().split())


for i in range(case):
    r = int(T[i][0])
    s = T[i][1]

    ans = ''
    
    for j in range(len(s)):
        ans += s[j] * r
    print(ans)
