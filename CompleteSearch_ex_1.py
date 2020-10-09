"""
Date : 10/09/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/42840
Description : Brute Force search algorithm
"""
# My Answer
answer = []
answers = [1, 3, 2, 4, 2]

one = [1,2,3,4,5]
two = [2,1,2,3,2,4,2,5]
three = [3,3,1,1,2,2,4,4,5,5]

score_1 = 0
score_2 = 0
score_3 = 0

x = 0

while x < len(answers):
    print("num of x : ", x)

    if one[x%5] == answers[x]:
        score_1 += 1
    if two[x%8] == answers[x]:
        score_2 += 1
    if three[x%10] == answers[x]:
        score_3 += 1
    
    x += 1

winner = max(score_1, score_2, score_3)

if winner == score_1 :
    answer.append(1)
if winner == score_2 :
    answer.append(2)
if winner == score_3 :
    answer.append(3)
        
print(answer)


# Popular Answer
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
