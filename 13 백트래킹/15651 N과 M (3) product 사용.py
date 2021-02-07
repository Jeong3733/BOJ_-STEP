from itertools import product

N, M = map(int, input().split())
nums = [str(num) for num in range(1, N+1)]
print("\n".join(list(map(" ".join, product(nums, repeat=M)))))