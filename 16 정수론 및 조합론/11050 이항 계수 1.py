cache = [[-1]*100 for _ in range(100)]
def bino(n, r):
    if r==0 or n==r:
        return 1
    if cache[n][r] != -1:
        return cache[n][r]
    
    cache[n][r] = bino(n-1, r-1) + bino(n-1, r)
    return cache[n][r]

n, r = map(int, input().split())
print(bino(n, r))