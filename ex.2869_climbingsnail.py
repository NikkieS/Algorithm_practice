'''
Date : 11/10/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2869
Description : find how many days it takes to reach the top
'''

a,b,v = map(int, input().split())   #a: up scale / b: down scale / v: top

# My Answer
'''
A=2 B=1 V=5
        start   end
day 1.    2      1
day 2.    3      2
day 3.    4      3
day 4.    5      4

<<pattern>>
start : up by A-B
'''

cost = a - b
days = 1

while a < v :
    
    a += cost
    days += 1

print(days)

# Short Coding
k = (v-b)/(a-b)

print(int(k) if k == int(k) else int(k)+1)
