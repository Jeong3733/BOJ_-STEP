from itertools import combinations

N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
biggest = 0
com = list(map(sum, combinations(nums, 3)))

for i in range(len(com)):
    if biggest < com[i] and com[i] <= M:
        biggest = com[i]

print(biggest)