from sys import stdin

N = int(stdin.readline())

# 입력받은 숫자를 저장할 리스트
arr = []

# 빈도를 저장할 딕셔너리 
Dic = {key : 0 for key in range(-4000, 4001)}

# 입력받으면서 빈도 저장
for _ in range(N):
    tmp = int(stdin.readline())
    arr.append(tmp)
    Dic[tmp] += 1

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
most = max(Dic.values())

# 최빈값과 같은 빈도로 나온 수들을 전부 저장
most_list = [key for key, frq in Dic.items() if frq == most]

if len(most_list) == 1:
    print(most_list[0])
else:
    print(most_list[1])

# 범위
rng = arr[-1] - arr[0]
print(rng)