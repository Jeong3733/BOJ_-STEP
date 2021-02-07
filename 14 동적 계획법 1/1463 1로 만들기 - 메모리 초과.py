import sys

sys.setrecursionlimit(10**9)

# 메모리 초과 발생
def makeOne(num):
    if num == 1:
        return 0

    if cache[num] != -1:
        return cache[num]

    ret = 50
    if num % 3 == 0:
        ret = min(ret, 1 + makeOne(num//3))
    if num % 2 == 0:
        ret = min(ret, 1 + makeOne(num//2))
    # 요 밑에 조건 넣어주니까 재귀호출 수가 줄어들어서 되는 듯?
    if num % 3 != 0 or num % 2 != 0:
        ret = min(ret, 1 + makeOne(num-1))

    cache[num] = ret
    return cache[num]

N = int(input())

cache = [-1] * (N+1)

print(makeOne(N))