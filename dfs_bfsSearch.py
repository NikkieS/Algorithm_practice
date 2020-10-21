"""
Date : 10/19/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/43165
Description : dfs / bfs
"""

def solution(numbers, target):
    n = len(numbers)
    cnt = 0

    def dfs(L, total):
        print("L: ", L)
        print("total: ", total)
        print("===============================")
        if L == n :
            if total == target :
                nonlocal cnt
                cnt += 1
        else :
            dfs(L+1, total+numbers[L])
            dfs(L+1, total-numbers[L])

    dfs(0,0)
    
    return cnt


def sol(numbers, target):
    cnt = 0
    len_numbers = len(numbers)

    def operator(idx=0):
        if idx < len_numbers:
            numbers[idx] *= 1
            print("더하기 idx:", idx, "list:", numbers)
            operator(idx+1)

            numbers[idx] *= -1
            print("빼기 idx:", idx, "list:", numbers)
            operator(idx+1)

        elif sum(numbers) == target:
            print("정답 idx:", idx, "list:", numbers)
            nonlocal cnt
            cnt += 1

    operator()

    return cnt

print(sol([1, 1, 1, 1, 1], 3))
