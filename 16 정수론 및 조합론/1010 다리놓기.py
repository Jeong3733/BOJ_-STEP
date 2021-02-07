import sys
cache = [[-1]*1001 for _ in range(1001)]

sys.setrecursionlimit(10**9)

def bino(n, r):
    if r==0 or n==r:
        return 1
    if cache[n][r] != -1:
        return cache[n][r]
    
    cache[n][r] = (bino(n-1, r-1) + bino(n-1, r))
    return cache[n][r]

N = int(input())

ans = []
for i in range(N):
    r, n = map(int, input().split())    
    ans.append(bino(n, r))

print(*ans, sep="\n")