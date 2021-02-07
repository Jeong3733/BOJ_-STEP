N = int(input())

cache = [-1] * (N+1)

cache[0], cache[1] = 0, 0

for i in range(2, N+1):
    ret = 10**6

    if i%3 == 0:
        ret = min(ret, cache[i//3] + 1)
    if i%2 == 0:
        ret = min(ret, cache[i//2] + 1)
    ret = min(ret, cache[i-1] + 1)

    cache[i] = ret

print(cache[N])