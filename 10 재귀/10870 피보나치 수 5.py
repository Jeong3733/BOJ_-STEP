N = int(input())

# fib[n] == -1 이면 아직 계산 X
fib = [-1 for i in range(N+1)]

def fibo(n):
    # 기저 사례 : n==0, n==1
    if n==0:
        return 0
    if n==1:
        return 1

    # 미리 저장해둔 곳에 결과가 없으면 재귀 호출해서 계산
    if fib[n] == -1:
        fib[n] = fibo(n-1) + fibo(n-2)

    return fib[n]

print(fibo(N))