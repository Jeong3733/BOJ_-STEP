import sys

sys.setrecursionlimit(10**9)

# index부터 시작하는 부분 수열 중, 가장 긴 증가하는 부분 수열의 길이
def LIS(index):
    if cache[index] != -1:
        return cache[index]

    ret = 1
    for num in range(index+1, N):
        if seq[num] > seq[index]:
            ret = max(ret, LIS(num)+1)
    cache[index] = ret
    return ret

N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
cache = [-1] * N


ans = -10**9
for i in range(N):
    ans = max(ans, LIS(i))

print(ans)

"""
6
10 20 10 30 20 50
"""