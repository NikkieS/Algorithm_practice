# 선수의 수 <= 100,000
# completion < participant (1)
# 참가자 동명이인 있을 수 있음

from collections import Counter

def solution(participant, completion):
    answer = ''
    
    return answer

participant = ["mislav", "stanko", "mislav", "ana"]    # 참가자
completion = ["stanko", "ana", "mislav"]   # 완주자


#print(list(filter(lambda x: x not in completion, participant)))
res = map(lambda x: participant.remove(x), completion)
print(list(res))

print(list((Counter(participant) - Counter(completion)).elements()))


# hash를 사용한 풀이
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
