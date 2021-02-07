import sys

N = int(input())
cache = [[0]*9 for _ in range(N)]

for i in range(len(cache[0])):
    cache[0][i] = 1

# 길이가 2 ~ N까지 
for digit in range(1, N):
    # 첫번째 숫자가 1~9까지
    for firstNum in range(9):
        # 첫번쨰
        if firstNum == 0 and digit > 1:
            # 맨 오른쪽에 1더한건 0,1로만 이루어진 계단 수
            cache[digit][firstNum] = cache[digit-1][firstNum+1] + cache[digit-2][firstNum]
        elif firstNum == 8:
            cache[digit][firstNum] = cache[digit-1][firstNum-1]
        else:
            cache[digit][firstNum] = cache[digit-1][firstNum+1] + cache[digit-1][firstNum-1]

print(sum(cache[N-1]) % 10**9)