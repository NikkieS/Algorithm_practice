#1. 두 수의 차 구하기 - 큰 수에서 작은 수
'''
1. 숫자 두개를 받는다
2. a와 b를 비교한다
3. 큰 수에서 작은 수를 빼준다
4. 결과를 출력해준다
'''

num1 = int(input('숫자를 입력하세요 : '))
num2 = int(input('다른 숫자를 입력하세요 : '))

def subtraction(num1, num2):
    result = 0
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
    return result

print(comparison(num1, num2))

#2. 두 수의 차 구하기 - 절대값을 이용하는 방법
'''
1. 숫자 두개를 받는다
2. 절대값의 차를 출력해준다
'''

num1 = int(input('숫자를 입력하세요 : '))
num2 = int(input('다른 숫자를 입력하세요 : '))

def absolute(num1, num2):
    return abs(num1 - num2)

print(absolute(num1, num2))

#3. 짝수와 홀수 판별하기
'''
1. 숫자를 받는다
2. 만약 2로 나눈 나머지가 0이면 결과값은 짝수 아니면 홀수로 판단
3. 결과값 출력
'''

num = int(input('숫자를 입력하세요 : '))

def even_odd(num):
    if num % 2 == 0:
        result = '짝수'
    else:
        result = '홀수'

    return result

print(even_odd(num))

#4. 두 수중 큰 수 찾기
'''
1. 숫자 두개를 받는다
2. 비교하여 큰수를 반환해 준다
3. 만약 같은 숫자이면 같다고 반환해 준다
'''

num1 = int(input('숫자를 입력하세요 : '))
num2 = int(input('다른 숫자를 입력하세요 : '))

def comparison(num1, num2):
    if num1 > num2:
        result = str(num1) + '가 더 큽니다.'
    elif num1 == num2:
        result = '같다'
    else:
        result = str(num2) + '가 더 큽니다.'

    return result

print('가장 큰 수 =', comparison(num1, num2))

#5. 세 수중 가장 큰 수 찾기 - 두 가지 방법
'''
1. 숫자 세개를 받는다
2. 비교하여 큰수를 반환해 준다
3. 만약 같은 숫자이면 같다고 반환해 준다
'''

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))
num3 = int(input('세번째 숫자를 입력하세요 : '))

def compare_three1(num1, num2, num3):
    if num1 < num2 < num3:
        return num3
    elif num1 < num3 < num2:
        return num2
    elif num1 == num2 == num3:
        return '모두 같음'
    else:
        return num1

print(compare_three1(num1, num2, num3))

def compare_three2(num1, num2, num3):
    if num1 == num2 == num3:
        return '모두 같음'
    else:
        return max(num1, num2, num3)

print('가장 큰 수 =', compare_three2(num1, num2, num3))

#6. 최대값 찾기
'''
1. N개의 숫자를 자료구조로 받는다
2. 최대값을 반환해 준다
'''
l1 = [1,2,3,4,5,6,7,8]
t1 = (2,5,8,1,3,9)
d1 = {1: 'c', 2: 'b', 3: 'a'}

def max_num(num_lst) :
    return max(num_lst)

print(max_num(l1))

#7. 두 변수 값 교환하기
'''
1. 두개의 변수 선언
2. 교환하기
'''
x = 3
y = 5

x,y = y,x

print('x = ', x, 'y = ', y)

#8. 작은 수에서 큰 수 까지의 합 구하기
'''
1. 작은 수와 큰 수를 받는다
2. 큰 수를 result라는 변수로 저장해준다
3. result에 큰 수보다 하나 작은 수를 더해준다
4. 3번 작업을 while문을 돌려 반복해준다
5. 큰 수를 하나씩 줄여주면서 내려준다
6. 큰 수가 작은 수와 같아질때 까지 반복해준다
'''

low = int(input('작은 수를 입력하세요 : '))
high = int(input('큰 수를 입력하세요 : '))

def low_to_high(low, high):
    result = high
    while high > low :
        result += high - 1
        high = high -1
        print('high =', high, 'result =', result)

    return result

print(low_to_high(low, high))

#9. 특정 숫자 까지의 3의배수 합 구하기
'''
1. 특정숫자를 받는다
2. 들어오는 숫자마다 3을 곱해주고 다음 숫자와 합해준다
3. 숫자가 1이 될때까지 특정숫자에서 1씩 줄이며 재귀호출해준다
4. 1이 되면 3의 배수인 3을 반환해준다
'''
def multi_three(num) :
    if num <= 1 :   # 숫자가 1이 되면
        return 3    # 3의 배수인 3을 반환해준다
    return num * 3 + multi_three(num - 1)   #들어오는 숫자마다 3을 곱해주고 다시 함수를 호출해서 결과를 더해준다 대신 다음 수는 1을 빼서 내려준다

#10. 1, -2, 3, -4,... , -100 합 구하기
'''
1. 새로운 변수를 생성한다
2. 새로운 변수의 값을 짝수인 경우 음수로 바꾸고 홀수인 경우 그대로 유지하여 넣어준다 
3. 만들어진 새로운 변수와 다음 숫자를 합해준다
4. 들어오는 숫자를 1씩 줄이며 함수를 재귀호출해준다
5. 1이되면 1을 반환한다
'''
def sum(num):
    if num % 2 == 0:    #2로 나누어 나머지가 0이 되면 짝수
        new_num = num * -1  #음수로 바꾸어 새로운 변수로 저장
    else:   #홀수인경우
        new_num = num   #새로운 변수는 홀수값을 그대로 넣어준다
    if num == 1:    #재귀호출이 1까지 내려오게 되면
        return 1    #1을 반환

    return new_num + sum(num - 1)   #-100 + 99 + -98 + ..... + 1 순으로 돌아가게된다

print(sum(100))

