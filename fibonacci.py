'''
Date : 10/22/20
Author : GaRam Song
Description : fibonacci practice
'''
def fib_recur(x):
    if x==0 or x==1:
        return x
    else :
        return fib(x-1) + fib(x-2)

def fib_iter(x):
    
    temp = [0, 1]

    if x > 1:
        for i in range(2, x+1):
            temp.append(temp[i-1] + temp[i-2])

    return temp[x]

def fib_iter_ex(x):
    num1 = 0
    num2 = 1
    num3 = 0

    if x == 0 or x == 1:
        return x

    else:
        for i in range(1, x):
            num3 = num1 + num2
            num1 = num2
            num2 = num3

    return num3

print(fib_iter(30))
