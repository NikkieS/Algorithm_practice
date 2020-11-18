'''
Date : 11/18/20
Author : GaRam Song
URL : https://acmicpc.net/problem/10250
Description : when h tall and w wide hotel assigns rooms from bottom left to top right,
              find the room num of Nth guest
'''

T = int(input())

ans = []

for _ in range(T):
    h, w, n = map(int,input().split())

    y = n%h
    x = n//h
   
    ans.append(h*100+x if y==0 else y*100+(x+1))
    
for i in range(len(ans)):
    print(ans[i])
