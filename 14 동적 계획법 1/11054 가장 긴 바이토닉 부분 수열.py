import sys

def right(index):
    if rCache[index] != -1:
        return rCache[index]
    
    ret = 1
    for i in range(index+1, N):
        if seq[index] > seq[i]:
            ret = max(ret, right(i) + 1)
    rCache[index] = ret
    return rCache[index]


def left(index):
    if lCache[index] != -1:
        return lCache[index]
    
    ret = 1
    for i in reversed(range(index)):
        if seq[index] > seq[i]:
            ret = max(ret, left(i) + 1)
    lCache[index] = ret
    return lCache[index]


N = int(input())
seq = list(map(int, sys.stdin.readline().split()))
rCache = [-1] * N
lCache = [-1] * N

ans = -1
for index in range(N):
    ans = max(ans, left(index) + right(index) - 1)
print(ans)

"""
10
1 5 2 1 4 3 4 5 2 1
"""