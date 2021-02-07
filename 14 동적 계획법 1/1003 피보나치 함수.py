from sys import stdin
def fibo(n):
    # 기저 사례 : n==0, n==1 일 때
    if n==0: 
        return 1, 0
    elif n==1:
        return 0, 1

    # 미리 저장해둔 곳에 결과가 없으면 재귀 호출해서 계산 (메모이제이션)
    if fib[n][0] == -1 or fib[n][1] == -1:
        n1_zero, n1_one = fibo(n-1)
        n2_zero, n2_one = fibo(n-2)

        fib[n][0] = n1_zero + n2_zero        
        fib[n][1] = n1_one + n2_one

    return fib[n][0], fib[n][1]


T = int(stdin.readline())
case = [int(stdin.readline()) for _ in range(T)]
Max = max(case)

fib = [[-1]*2 for _ in range(Max+1)]
fib[0][0], fib[0][1] = 1, 0
fib[1][0], fib[1][1] = 0, 1

fibo(Max)

for i in case:
    # print(*fib[i])
    print(" ".join(map(str, fib[i])))

"""
3
0
1
3
"""