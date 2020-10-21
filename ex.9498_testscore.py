"""
Date : 10/21/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/9498
Description : test letter score
"""

score = int(input())

if score >= 60 :
    ans = "D"
    
    if score >= 70 :
        ans = "C"

        if score >= 80 :
            ans = "B"

            if score >= 90 :
                ans = "A"
else :
    ans = "F"

print(ans)

print('FFFFFFDCBAA'[int(input())//10])
