"""
Date : 10/08/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/42748
Description : array sorting algorithm
"""

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# My Answer
from operator import itemgetter

def solution(array, commands):
    answer = []
    
    for x in range(0, 3):
        i = commands[x][0] # i
        j = commands[x][1] # j
        k = commands[x][2] # k

        
        new = sorted(array[i-1:j])    #i~j 까지의 배열
        answer.append(new[k-1])
        
        #new = sorted(array[commands[x][0]-1:commands[x][1]])
        
        #answer.append(new[commands[x][2]-1])
        
    return answer

# Popular Answer
def solution(array, commands):

    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))



