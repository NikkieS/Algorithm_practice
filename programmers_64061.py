'''
Date : 10/29/20
Author : GaRam Song
URL : https://programmers.co.kr/learn/courses/30/lessons/64061
Description : claw machine game using array list
'''
# My Answer
def solution(board, moves):
    basket = []
    ans = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                basket.append(board[j][i-1])
                print('j:',j,'i:',i,'basket:', basket)
                board[j][i-1] = 0
                if basket[-1:] == basket[-2:-1]:
                    ans += 2
                    basket = basket[:-2]
                break
    return ans

# Popular Answer
def sol(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))
