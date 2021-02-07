def bck_trk4(picked, toPick):
    if toPick == 0:
        print(*picked)
        return
    
    if picked:
        start = max(picked)
    else:
        start = 1
    
    for num in range(start, N+1):
        picked.append(num)
        bck_trk4(picked, toPick-1)
        picked.pop()

N, M = map(int, input().split())
picked = []
bck_trk4(picked, M)