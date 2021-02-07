N = int(input())

per_info = []
rank = [1 for i in range(N)]

for tuples in range(N):
    per_info.append(tuple(map(int, input().split())))

"""
for cmp1 in per_info:
    for cmp2 in per_info:
        if cmp1[0] < cmp2[0] and cmp1[1] < cmp2[1]:
            # 인덱스로 접근시, 똑같은 원소가 있을 경우에 문제가 생김
            rank[per_info.index(cmp1)] += 1

for ans in rank:
    print(ans, end=" ")
"""

for cmp1 in per_info:
    ranks = 1
    for cmp2 in per_info:
        if cmp1[0] < cmp2[0] and cmp1[1] < cmp2[1]:
            ranks += 1
    print(ranks, end=" ") 



