'''
Date : 10/26/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/2941
Description : count length of a croatian word
'''
# My Answer
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for letter in alph :
    word = word.replace(letter,"@")

print(len(word))

# Short Coding
c=input().count;print(c('')+~sum(map(c,'- = nj lj dz='.split())))
