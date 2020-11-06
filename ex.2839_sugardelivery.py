'''
Date : 11/04/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2839
Description : least number of divisions by 5 and 3 until 0
'''

order = int(input())
bag = 0

while True:
    if order % 5 == 0 : #check if num is divisible by 5
        bag = bag + (order//5)  # add divisor to the return value
        break

    order = order -3    #if not divisible by 5 -> subtract 3 gradually
    bag += 1
    
    if order < 0:   #if not divisible by 5 or 3 -> return -1
        bag = -1
        break

print(bag)

