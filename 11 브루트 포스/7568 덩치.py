N = int(input())

per_info = []
rank = [1 for i in range(N)]

for tuples in range(N):
    per_info.append(tuple(map(int, input().split())))

for cmp1 in range(N):
    for cmp2 in range(N):
        if (per_info[cmp1][0] < per_info[cmp2][0] and 
            per_info[cmp1][1] < per_info[cmp2][1]):
            rank[cmp1] += 1

for ans in rank:
    print(ans, end=" ")