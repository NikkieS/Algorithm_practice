'''
Date : 11/02/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/42862
Description : find a soltuion by Greedy algorithm
'''
n = 5
lost= [2,4]
reserve = [1,3]

#My Answer
def sol(n, lost, reserve):
    # removing possible duplicates from the two lists
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)

    for i in set_reserve:
        if i-1 in set_lost: # finding the previous student first
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
            
    return n-len(set_lost)

'''
1. collection set allows operation of another set
2. optimal way of solving this problem is to try finding
    number previous to the element in 'reserve' first 
'''
