'''
Date : 10/24/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2908
Description : find the bigger number read backwards
'''

num = input()
first = ''
second = '' 

for i in range(len(num)-1, 3, -1) :
    first += num[i]

for i in range(2, -1, -1) :
    second += num[i]

if first > second :
    print(first)
else :
    print(second)

