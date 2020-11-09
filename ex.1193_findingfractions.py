'''
Date : 11/09/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/1193
Description : find the fraction number from a list after a given number of moves
'''

num = int(input())

# My Answer
'''
1. 가로 진행 :       idx[0] = 0 & idx[1] = even
2. 대각선 내려가기 : idx[0] = 0 & idx[1] = odd
    - idx[1] = 0 이 될때까지 반복
3. 대각선 올라가기 : idx[1] = 0 & idx[0] = even
    - idx[0] = 0 이 될때까지 반복
4. 세로 진행 :       idx[1] = 0 & idx[0] = odd
'''
idx = [0,0]

if num == 1 :
    print('1/1')
else:
    idx = [0,1]
    num -= 2
    while num > 0 :

        
        # 가로 진행
        if idx[0] == 0 and idx[1] % 2 == 0 :
            #print('가로진행:',idx)
            idx[1] += 1

            num -= 1
      
        # 대각선 내려가기
        elif idx[0] == 0 and idx[1] % 2 != 0 :
            while idx[1] != 0 and num > 0 :
                #print('대각선 내려가기:',idx)
                idx[0] += 1
                idx[1] -= 1

                num -= 1
        # 대각선 올라가기
        elif idx[1] == 0 and idx[0] % 2 == 0 :
            while idx[0] != 0 and num > 0 :
                #print('대각선 올라가기:',idx)
                idx[0] -= 1
                idx[1] += 1

                num -= 1
          
        # 세로 진행
        elif idx[1] == 0 and idx[0] % 2 != 0 :
            #print('세로진행:',idx)
            idx[0] += 1

            num -= 1
        
    print('{}/{}'.format(idx[0]+1,idx[1]+1))
 

# Faster Code
'''
 stage |     num     |      fraction      | denominator + numerator
   1          1              1/1                        2
   2         2,3           1/2, 2/1                     3
   3        4,5,6         3/1,2/2,1/3                   4
   4       7,8,9,10     1/4,2/3,3/2,4/1                 5
   5    11,12,13,14,15 5/1,4/2,3/3,2/4,1/5              6

<< pattern >>
1. stage + 1 = denom+num
2. stage = number of nums (num of fractions)
3. even num stage : denom = + 1~ / numer = stage - 1
4. odd num stage : denom = stage - 1~ / numer = + 1~
'''
stage, key = 1, 1

while key + stage <= num :
    key += stage
    stage += 1
    #print('key:', key, 'stage:', stage)

# moves from the first num in a stage
step = num - key
x, y = step + 1, stage - step

if stage % 2 == 0 :
    print('{}/{}'.format(x,y))
else :
    print('{}/{}'.format(y,x))
    
