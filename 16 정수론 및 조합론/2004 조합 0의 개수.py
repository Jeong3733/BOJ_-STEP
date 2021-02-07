n, r = map(int, input().split())

def getTrailingZeroes(n):
    two, five = 0, 0
    
    i = 2
    while i <= n:
        two += n // i
        i = i*2

    i = 5
    while i <= n:
        five += n // i
        i = i*5

    return two, five

print(min(getTrailingZeroes(n)[0] - (getTrailingZeroes(n-r)[0] + getTrailingZeroes(r)[0]),
          getTrailingZeroes(n)[1] - (getTrailingZeroes(n-r)[1] + getTrailingZeroes(r)[1])))
