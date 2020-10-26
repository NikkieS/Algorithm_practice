'''
Date : 10/24/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/5622
Description : dial
'''

'''
{'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
65 - 67 : 2 => 1,2,3
68 - 70 : 3 => 4,5,6
71 - 73 : 4 => 7,8,9
74 - 76 : 5 => 10,11,12
77 - 79 : 6 => 15
80 - 83 : 7 => 19
84 - 86 : 8 => 23
87 - 90 : 9 => 26

'''
# My Answer
word = input()

time = 0

for letter in word :
    asc = ord(letter)

    if asc > 86 :
        time += 10
    elif asc > 83 :
        time += 9
    elif asc > 79 :
        time += 8
    elif asc > 76 :
        time += 7
    elif asc > 73 :
        time += 6
    elif asc > 70 :
        time += 5
    elif asc > 67 :
        time += 4
    else :
        time += 3

print(time)

# Alternative Answer
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)

# Short Coding
print(sum(62-int(10000/(ord(v)+102))for v in input()))
