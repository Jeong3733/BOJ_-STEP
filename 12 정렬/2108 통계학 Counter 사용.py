from sys import stdin
from collections import Counter

N = int(stdin.readline())

# 입력받은 숫자를 저장할 리스트
arr = [int(stdin.readline()) for _ in range(N)]

# 값들을 정렬
arr  = sorted(arr)

# 평균, 파이썬 range 함수는 짝수면 내림이라서 따로 만듬
if sum(arr)/N - sum(arr)//N >= 0.5:
    avg = sum(arr) // N + 1
else:
    avg = sum(arr) // N
print(avg)

# 중앙값
mid_val = arr[N//2]
print(mid_val)

# 최빈값
most = Counter(arr).most_common()
sortedArr = sorted(list(Counter(arr).items()), key = lambda x:x[1])

if len(most) > 1:
    print(most[1][0])
else:
    print(most[0][0])

# 범위
rng = arr[-1] - arr[0]
print(rng)