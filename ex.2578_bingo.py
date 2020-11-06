"""
Date : 11/06/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2578
Description : bingo
"""

def isBingo(check) :
    '''
    check list contains 1s where I got it right on my bingo plate
    0 : wrong
    1 : correct
    '''
    
    bingo_cnt = 0
    check_T = list(map(list,zip(*check)))
    '''
    zip() function returns : tuple
    zip(*iterable) : unzipps the list
    coordinate & value swap -> row and column swap
    '''
    
    # row&column bingo check
    for i in range(5) :
        if 0 not in check[i] :      # row bingo
            bingo_cnt += 1
        if 0 not in check_T[i] :    # column bingo
            bingo_cnt += 1
            
    # diagonal bingo check
    r_flag, l_flag = True, True
    for i in range(5) :
        if check[i][i] == 0:    # From top left to bottom right
            r_flag = False
        if check[i][4-i] == 0:  # From top right to bottom left
            l_flag = False

    if r_flag:
        bingo_cnt += 1
    if l_flag:
        bingo_cnt += 1

    if bingo_cnt >= 3:
        return True

    return False

    
bingo = []
calls = []
check = [[0 for i in range(5)] for i in range(5)]
count = 0

for i in range(5):
    bingo.append(list(map(int, input().split())))

for j in range(5):
    calls.append(list(map(int, input().split())))


for k in range(5):
    for l in range(5):
        if bingo[k][l] == calls[k][l]:
            check[k][l] = 1
            k = 5
            break
        
# check if bingo
for call in calls :
    while call: # one row of answers
        num = call.pop(0)
        count += 1

        # make a check list where the answer is in my bingo plate 
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == num:
                    check[i][j] = 1
                    i = 5   # break from the i loop
                    break

        if count >= 12:
            if isBingo(check) == True :
                print(count)
                break
    else :
        # Continue if the inner loop wasn't broken
        continue
    # Inner loop was broken, break the outer
    break

