'''
Date : 10/27/20
Author : GaRam Song
URL : https://www.acmicpc.net/problem/1316
Description : letter repeat words
'''
#My Answer
num = int(input())
count = 0

for i in range(num):
    word = input()
    check = []

    for i in range(len(word)) :
        if word[i] not in check :
            check.append(word[i])
            
        elif word[i] != check[-1] :
            count += 1
            break

print(num-count)

# Short Coding
r=0;i=input;exec('s=i();r+=[*s]==sorted(s,key=s.find);'*int(i()));print(r)

'''
1. [*str] : letter하나씩 넣어줌
    [*'happy'] => ['h', 'a', 'p', 'p', 'y']

2. sorted( ) key= str.find 로 두면 str의 들어온 character순으로 정렬이 된다
    s = ['abca'], sorted(s, key = s.find) => ['a', 'a', 'b', 'c']

풀이

s = 'abca'라고 가정

1. [*s]==sorted(s,key=s.find) 실행하게 되면
    ['a','b','c','a'] == ['a', 'a', 'b', 'c'] : 값은 False (== 0)
2. r+= False -> r += 0
3. int(input()) 만큼 수행 하고 r 출력
'''
