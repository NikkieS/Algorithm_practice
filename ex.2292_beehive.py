'''
Date : 11/07/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2292
Description : if each cell in a beehive is numbered from the center out
              how many cells are needed to travel from the center cell
              to a given numbered cell
'''

'''
1st wrap. 1 cell : 1
2nd wrap. 6 cells : 2,3,4,5,6,7 (6*1)
3rd wrap. 12 cells : 8,9,10,11,12,13, ..., 19 (6*3)
4th wrap. 18 cells : 20,21,22, ..., 37 (6*6)
5th wrap. 24 cells : 38,39,40, ..., 61 (6*10)
'''

num = int(input())
x = 1
y = 0

if num == 1:
    print(1)
else :
    while True:
        
        end = 6*(y+x)+1 # last cell num is is an increment of 6 plus 1
        
        print('x:',x,'y:',y,'end:',end)
        
        if num <= end : # last cell num is equal or greater
            print(x+1)
            break
        y = y+x
        x += 1
