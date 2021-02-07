import sys

sys.setrecursionlimit(10**9)

# n : 수열의 크기
# end : 마지막 원소의 최대합 계산시 포함 여부.
# end=0 -> 마지막 원소를 제외했을 때, 가장 큰 연속 합
# end=1 -> 마지막 원소를 포함했을 때, 가장 큰 연속 합

# 점화식
# cntiSum(n, 0) = max(cntiSum(n-1, 0), cntiSum(n-1, 1))
# cntiSum(n, 1) = max(cntiSum(n-1, 1) + arr[n], arr[n]) -> arr[n]이 음수일 경우 걸러내주기 위해
# https://folivora.tistory.com/89 -> 필독

def cntiSum(n, endWithLast):
    if n == 0:
        return arr[0]
    if cache[n][endWithLast] != None:
        return cache[n][endWithLast]

    if endWithLast == 0:
        cache[n][0] = max(cntiSum(n-1, 0), cntiSum(n-1, 1))
    if endWithLast == 1:
        cache[n][1] = max(cntiSum(n-1, 1) + arr[n], arr[n])

    return cache[n][endWithLast]


N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
cache = [[None]*2 for _ in range(N)]

print(max(cntiSum(N-1, 0), cntiSum(N-1, 1)))

"""
10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5
"""

# def cntiSum(n):
#     if n == 0:
#         return arr[0]
#     if cache[n] != None:
#         return cache[n]

#     tmp = arr[n]
#     maxi = -10**8
#     for i in reversed(range(n)):
#        tmp += arr[i]
#        maxi = max(maxi, tmp)
#     cache[n] = max(cntiSum(n-1), maxi)
#     return cache[n]