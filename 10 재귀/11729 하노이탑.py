def hanoi(n, start, via, dest):
    # 기저사례 : n == 1
    if n == 1:
        print(start, dest)
        return

    # 하노이 탑의 기본 원리는 n-1개의 원판을 경유지점에 옮긴다음   ...   1
	# 가장 큰 원판을 도착지에 옮기고   ...   2
	# 나머지 n-1개의 원판을 도착지점에 옮기는 것이다.   ...   3
    hanoi(n - 1, start, dest, via) # 1
    hanoi(1, start, via, dest) # 2
    hanoi(n - 1, via, start, dest) # 3

N = int(input())

# 아래 함수에서 점화식을 구해보면, f(1) = 1, f(n) = 2*f(n-1) + 1이므로
# 일반항을 구해보면 f(n) = 2^(n) - 1이다.
print(2 ** N - 1)
hanoi(N, 1, 2, 3)