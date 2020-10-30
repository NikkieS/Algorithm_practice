'''
Date : 10/30/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/68644
Description :
    add two numbers from a list and return a new list with additions
    without duplicates
'''
from itertools import combinations

#My Answer
'''
collection set()
1. no duplicates
2. immutable (though add, remove allowed)
3. unordered
'''
def solution(numbers) :
    answer = set()  #set cannnot have duplicates

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    
    return answer

# Short Coding 1
answer = set()
for i in list(combinations(numbers,2)):
    answer.add(sum(i))

print(sorted(answer))

# Short Coding 2
print(sorted(list(set([sum([i,j]) for i, j in combinations(numbers,2)]))))

