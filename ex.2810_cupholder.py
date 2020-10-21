"""
Date : 10/19/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2810
Description : find how many people can use the cupholder at a movie theater
"""

N = int(input())    # num of people in a row
seats = input()      # seating arrangement

couple = seats.count("LL")   # num of couples


if couple <= 1 :    
    print(N)
else :
    print(N - couple + 1)


cup = 1
flag = 0

for seat in seats:
    if seat == "S":
        cup += 1
    else :
        if flag == 0 :
            flag = 1
        elif flag == 1:
             cup += 1
             flag = 0

print(min(cup, N))

cup = 1

for seat in seats:
    if seat == "S":
        cup += 1
    else :
        cup += 0.5

print(min(int(cup), N))
