N = int(input())
way = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 현재 i번째 도시. i+1번째 이후의 도시들 중에서
# cost[i]보다 싼 도시까지의 거리만큼 기름을 사감.
i, ret = 0, 0
while i < N-1:
    dist = 0    
    j = i+1
    # 기름 값이 더 싼 도시를 찾는 과정
    while j <= N-1:
        dist += way[j-1]
        if j >= N or cost[i] > cost[j]:
            break
        j += 1
    # 더 싼 도시를 찾는다면, 그동안 계산한 거리와 가격을 곱해서
    # 총 비용을 계산
    ret += dist * cost[i]
    i = j

print(ret)
    
"""
4
2 3 1
5 2 4 1

4
3 3 4
1 1 1 1
"""