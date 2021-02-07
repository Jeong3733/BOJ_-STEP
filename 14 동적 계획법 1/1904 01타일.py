N = int(input())

cache = [-1] * (N+2)

cache[1] = 1
cache[2] = 2

for i in range(3, N+1):
    cache[i] = (cache[i-1] + cache[i-2]) % 15746

print(cache[N])