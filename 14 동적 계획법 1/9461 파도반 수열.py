from sys import stdin

N = int(stdin.readline())
num = [int(stdin.readline()) for _ in range(N)]

cache = [-1] * 101

cache[1], cache[2], cache[3] = 1, 1, 1
cache[4], cache[5] = 2, 2

for i in range(6, max(num)+1):
    cache[i] = cache[i-1] + cache[i-5]

for index in num:
    print(cache[index])

"""
2
6
12
"""