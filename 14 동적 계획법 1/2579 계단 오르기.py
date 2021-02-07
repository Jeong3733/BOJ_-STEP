import sys

# 재귀호출의 깊이 설정(안해주면 런타임 에러)
sys.setrecursionlimit(10**9)

# n에서 도착 지점(N번째 계단)까지 가는 데 얻을 수 있는 최대 점수
def goUp(n, conti):
    # 152p 범위를 벗어난 경우 기저 사례로 처리하기
    # 반드시 원래 기저사례보다 먼저 검사하기 !!!
    # 기저 사례 : N번째 계단을 밟지 않은 경우, 3번 연속 같은 계단을 밟은 경우
    if n > N:
        return -10**9
    if conti >= 3:
        return -10**9

    # 기저 사례 : 도착지점에 온 경우
    if n == N:
        return stair[N]

    # 메모이제이션
    if cache[n][conti] != -1:
        return cache[n][conti]

    # 점화식 : D(n, conti) = score(n) + max(D(n+1, conti+1), D(n+2, 1))
    cache[n][conti] = stair[n] + max(goUp(n+1, conti+1), goUp(n+2, 1))
    return cache[n][conti]


N = int(input())

cache = [[-1] * 3 for _ in range(N+1)]

stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))

print(goUp(0, 0))

"""
6
10
20
15
25
10
20
"""