'''
Date : 11/11/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/12899
Description : translate numbers only using 1,2,4 (base3)
1 => 1
2 => 2
3 => 4
4 => 11
5 => 12
6 => 14
7 => 21
'''
num = int(input())

def check(num) :
    T = '124'
    
    if num <= 3 :   # because three numbers are available
        return T[num-1]
    else :
        # since T starts from 1 not 0
        q, r = divmod(num-1, 3) # do num-1
        return check(q) + T[r]


print(check(num))
