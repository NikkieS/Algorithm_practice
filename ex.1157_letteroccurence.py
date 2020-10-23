'''
Date : 10/23/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/1157
Description : find the letter that appears the most in a string
'''
# My Answer
from collections import Counter

word = input().upper()  # input 자체를 대문자로 변환해서 저장

occurence = {}

for letter in word :
    if letter in occurence: # 만약 딕셔너리에 이미 존재하면
        occurence[letter] += 1
    else :                  # 아니면 새로 key로 만들기
        occurence[letter] = 1

# max함수에 key를 value로 두기 -> 반환값 : key
ans = max(occurence, key = lambda x : occurence[x])

val = occurence[ans]

'''
Counter 는 dictionary로 반환
요소가 몇개가 들어있는지 확인
'''
if Counter(occurence.values())[val] > 1:
    print('?')
else :
    print(ans)

# Short Coding Answer
from statistics import*

try:t=mode(input().upper())
except:t='?'
print(t)
