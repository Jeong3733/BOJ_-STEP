N = int(input())

def fac(n):
    # 기저 사례 : n==0, n==1
    if n == 0 or n == 1:
        return 1

    # n번째 단계에서 n을 곱하는 역할
    return n * fac(n-1)

print(fac(N))