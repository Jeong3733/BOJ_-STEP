def bck_trk3(picked, toPick):
    if toPick == 0:
        print(*picked)
        return 
    
    for num in range(1, N+1):
        picked.append(num)
        bck_trk3(picked, toPick-1)
        picked.pop()

N, M = map(int, input().split())
picked = []
bck_trk3(picked, M)