def bck_trk2(picked, toPick):
    if toPick == 0:
        print(" ".join(map(str, picked)))
        return

    # 중복된 원소를 제거하기 위해서는 사전 순으로 가장 먼저오는 답 하나만 세도록 만들기 (가지치기)
    # 알고리즘 문제해결 전략 158p
    if picked:
        start = max(picked) + 1
    else:
        start = 1

    for pick in range(start, N+1):
        if pick in picked:
            continue
        picked.append(pick)
        bck_trk2(picked, toPick-1)
        picked.remove(pick)

N, M = map(int, input().split())
picked = []
bck_trk2(picked, M)