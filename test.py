# 두 수의 차 구하기 - 큰 수에서 작은 수
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

# 두 수의 차 구하기 - 절대값을 이용하는 방법
'''
1. 숫자 두개를 받는다
2. 절대값의 차를 출력해준다
'''

num1 = int(input('숫자를 입력하세요 : '))
num2 = int(input('다른 숫자를 입력하세요 : '))

def absolute(num1, num2):
    return abs(num1 - num2)

print(absolute(num1, num2))

# 짝수와 홀수 판별하기
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

# 두 수중 큰 수 찾기
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

# 세 수중 가장 큰 수 찾기 - 두 가지 방법
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


# 1, -2, 3, -4,... , -100 합 구하기

def sum(num):
    if num % 2 == 0:
        new_num = num * -1
    else:
        new_num = num
    if num == 1:
        return 1
    return new_num + sum(num - 1)


print(sum(100))

