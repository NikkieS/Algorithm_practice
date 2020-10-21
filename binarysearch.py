"""
Date : 10/20/20
Author : GaRam Song
Description : binary search
"""

def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1

    while lower <= upper :
        
        middle = (upper + lower) // 2

        print("lower :", lower)
        print("middle :", middle)
        print("upper :", upper)
              
        if L[middle] == x:
            idx = middle
            break

        elif L[middle] < x:
            lower = middle + 1

        else :
            upper = middle - 1

        print("------------------------")

    return idx

L = [2,3,5,6,9,11,15]
x = 9

print(solution(L, x))
