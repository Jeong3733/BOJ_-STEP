def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

N = int(input())
ans = 0
for i in reversed(str(factorial(N))):
    if i != '0':
        break
    ans += 1
print(ans)
