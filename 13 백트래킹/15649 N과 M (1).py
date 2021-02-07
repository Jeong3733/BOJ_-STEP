def bck_trk1(picked, toPick):
    global N

    if toPick == 0:
        print(" ".join(map(str, picked)))
        return
    
    for pick in range(1, N+1):
        if pick in picked:
            continue

        picked.append(pick)
        bck_trk1(picked, toPick-1)
        picked.remove(pick)

N, M = map(int, input().split())
picked = []
bck_trk1(picked, M)