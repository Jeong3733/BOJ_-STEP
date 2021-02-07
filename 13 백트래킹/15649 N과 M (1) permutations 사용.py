from itertools import permutations

N, M = map(int, input().split())
nums = [str(num) for num in range(1, N+1)]
print("\n".join(list(map(" ".join, permutations(nums, M)))))


