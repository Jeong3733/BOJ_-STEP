import sys

sys.setrecursionlimit(10**9)

def grape(n, conti):
    if n <= 0:
        return 0
    if conti >= 3:
        return -10**9

    if cache[n][conti] != -1:
        return cache[n][conti]

    cache[n][conti] = max(amt[n] + max(grape(n-1, conti+1), grape(n-2, 1)), grape(n-1, 1))
    return cache[n][conti]

N = int(input())

amt = [0]
for _ in range(N):
    amt.append(int(sys.stdin.readline()))

cache = [[-1]*3 for _ in range(N+1)]

print(grape(N, 1))

"""
6
9
9
1
1
9
9
"""