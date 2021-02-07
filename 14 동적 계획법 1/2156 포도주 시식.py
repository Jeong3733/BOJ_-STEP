import sys

sys.setrecursionlimit(10**9)

def grape(n, conti):
    if n > N:
        return 0
    if conti >= 3:
        return -10**9

    if cache[n][conti] != -1:
        return cache[n][conti]

    cache[n][conti] = amt[n] + max(grape(n+1, conti+1), grape(n+2, 1), grape(n+3, 1))
    return cache[n][conti]

N = int(input())

amt = [0]
for _ in range(N):
    amt.append(int(sys.stdin.readline()))

cache = [[-1]*3 for _ in range(N+1)]

print(grape(0, 0))

# 4칸까지 뛰는 거 계산하는 건 의미 없음
# (n+4 = n+2+2이고, 어차피 conti는 둘 다 1이므로 n+2+2가 무조건 많음)

# 3칸 뛰는 것이 이득인 경우를 생각해보면
# n+3 = n+1+2...(a) or n+2+1...(b) 인데,
# (b)는 실행 후 conti가 2이고, (a)는 n일 때 conti가 2이면 불가능하므로
# n일 때 conti가 2여도 실행 가능하고, 실행 후 conti가 1인 n+3이 필요
# 9 9 1 1 9 9 -> n+3이 없으면 이상한 답 나옴