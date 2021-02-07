from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = [str(num) for num in range(1, N+1)]
print("\n".join(list(map(" ".join, combinations_with_replacement(nums, M)))))