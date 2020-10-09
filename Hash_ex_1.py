"""
Date : 10/08/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/42576
Description : hash algorithm
"""
# 선수의 수 <= 100,000
# completion < participant (1)
# 참가자 동명이인 있을 수 있음

participant = ["mislav", "stanko", "mislav", "ana"]    # 참가자
completion = ["stanko", "ana", "mislav"]   # 완주자

# My Answer
from collections import Counter

def solution(participant, completion):
    
    return list((Counter(participant) - Counter(completion)).elements())[0]

#print(list(filter(lambda x: x not in completion, participant)))
#res = map(lambda x: participant.remove(x), completion)


# Answer using Hash
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
