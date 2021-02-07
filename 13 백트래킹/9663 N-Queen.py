def NQu(chess, col):
    if col == N:
        return 1
    
    ret = 0
    candidate = [num for num in range(N)]   

    for cnd in candidate:
        if cnd in chess:
            continue
        
        flag = True
        for exm in range(len(chess)):
            if (exm - col) ** 2 == (chess[exm] - cnd) ** 2 :
                flag = False
                break
        
        if flag:
            chess.append(cnd)
            ret += NQu(chess, col+1)
            chess.remove(cnd)

    return ret

N = int(input())
print(NQu([], 0))