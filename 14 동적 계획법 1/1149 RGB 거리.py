import sys

# 재귀호출의 깊이 설정(안해주면 런타임 에러)
sys.setrecursionlimit(10**9)

# n번째 집을 color로 칠할 때, 0 ~ n번째 집까지 칠하는 비용의 최솟값
def rgb(n, color):
    # 기저사례 : n이 0일때 까지 감소시켜가며 구함
    if n == 0:
        return cost[0][color]

    # color 이외의 색깔을 칠하기 위해서
    # 0:R    1:G    2:B
    cand = [0, 1, 2];    cand.remove(color)
    # candidate0, candidate1
    c0, c1 = cand[0], cand[1]

    # 메모이제이션
    if cache[n][color] != -1:
        return cache[n][color]

    # 점화식 : rgb(n, color0) = cost[n][color0] + min(rgb(n-1, color1), rgb(n-1, color2))
    cache[n][color] = cost[n][color] + min(rgb(n-1, c0), rgb(n-1, c1))
    return cache[n][color]


N = int(input())

cost = [[-1]*3 for _ in range(N)]
cache = [[-1]*3 for _ in range(N)]

for i in range(N):
    cost[i] = list(map(int, sys.stdin.readline().split()))

print(min(rgb(N-1, 0), rgb(N-1, 1), rgb(N-1, 2)))

"""
3
26 40 83
49 60 57
13 89 99
"""