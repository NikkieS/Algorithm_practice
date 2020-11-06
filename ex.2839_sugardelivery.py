'''
Date : 11/04/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2839
Description : least number of divisions by 5 and 3 until 0
'''

order = int(input())
bag = 0

while True:
    if order % 5 == 0 :
        bag = bag + (order//5)
        break

    order = order -3
    bag += 1
    
    if order < 0:
        bag = -1
        break

print(bag)

