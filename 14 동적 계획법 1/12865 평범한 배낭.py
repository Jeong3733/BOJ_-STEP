# 0 ~ n번째 물품까지 있을 때, 가치의 최댓값
# n : 현재 고르려는 물품의 index
# weight : 현재까지 고른 물품들의 무게

# 점화식
# bckpck(n, weight)
# if weight + w[n] > max   :   bckpck(n-1, weight)
# else   :   max(bckpck(n-1, weight), v[n] + bckpck(n-1, weight+w[n]))

def bckpck(n, weight):
    try:
        if n < 0:
            return 0
        if cache[n][weight] != -1:
            return cache[n][weight]

        if weight + w[n] > maxW:
            return bckpck(n-1, weight)
        else:
            cache[n][weight] = max(bckpck(n-1, weight), v[n] + bckpck(n-1, weight+w[n]))
        return cache[n][weight]

    except IndexError:
        print(n, weight)

N, maxW = map(int, input().split())
maxV, w, v = 0, [], []
for _ in range(N):
    tmp1, tmp2 = map(int, input().split())
    w.append(tmp1); v.append(tmp2)

cache = [[-1]*(maxW+1) for _ in range(N)]

print(bckpck(N-1, 0))

"""
4 7
6 13
4 8
3 6
5 12
"""