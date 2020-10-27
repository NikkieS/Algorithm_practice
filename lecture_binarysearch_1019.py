
def solution(L, x):
    lower = 0
    upper = len(L) - 1
    idx = -1
	
    while lower <= upper :
	middle = (upper + lower) // 2
		
	if L[middle] == x :
	    idx = middle
	    break
	elif L[middle] < x :
	    lower = middle + 1
	else :
	    upper = middle -1
    return idx
