'''
Date : 10/28/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/10809
Description : 
'''

S = input()
alph = [-1 for i in range(26)]
# 97 ~ 122 ascii code


for letter in S :
    alph[ord(letter)-97] = S.index(letter)  # index = 0

print(*alph)
