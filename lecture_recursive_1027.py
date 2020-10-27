def solution(L, x, l, u):
    if l > u:
        return -1
    
    mid = (l + u) // 2

    if x==L[mid] :
        return mid

    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    
    else :
        return solution(L, x, mid+1, u)

L = [2,5, 7, 9, 11]
x=4
l =0
u =4
print(solution(L, x, l, u))
