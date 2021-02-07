# index부터 시작하는 부분 수열 중, 가장 긴 증가하는 부분 수열의 길이
def LIS(index):
    if cache[index] != -1:
        return cache[index]

    ret = 1
    for num in range(index+1, N):
        if seq[num] > seq[index]:
            ret = max(ret, LIS(num)+1)
    cache[index] = ret
    return ret

N = int(input())
elec = [[0]*N for _ in range(N)]

# [idx][0] -> a, [idx][1] -> b
for idx in range(N):
    elec[idx][0], elec[idx][1] = map(int, input().split())
# a 기준으로 정렬
elec.sort(key=lambda x:x[0])

# a 기준으로 정렬된 b의 번호를 get
seq = [getB[1] for getB in elec]
cache = [-1] * len(seq)

tmp = -10**9
for i in range(N):
    tmp = max(tmp, LIS(i))

print(N-tmp)
