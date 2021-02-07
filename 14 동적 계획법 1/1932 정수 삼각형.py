from sys import stdin

# y, x에서 y == N까지 내려갈 때, 최대 비용을 구하는 함수
def tri(y, x):
    # 기저 사례 : y 좌표가 N-1일 때
    if y == N-1:
        return cost[y][x]

    # 메모이제이션
    if cache[y][x] != -1:
        return cache[y][x]

    # 점화식 -> a(y,x) = max(a(y+1, x+1), a(y+1, x)) + cost[y][x]
    cache[y][x] = cost[y][x] + max(tri(y+1, x), tri(y+1, x+1))
    return cache[y][x]

N = int(input())
cost = [[-1]* (i+1) for i in range(N)]
cache = [[-1]* (i+1) for i in range(N)]

for i in range(N):
    cost[i] = list(map(int, stdin.readline().split()))

print(tri(0, 0))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""