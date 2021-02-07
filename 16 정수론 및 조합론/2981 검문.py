from math import gcd
import sys

N  = int(sys.stdin.readline())

nums = []
sub = []

# 입력 받은 수들의 차를 저장.
for _ in range(N):
    inp = int(sys.stdin.readline())
    nums.append(inp)
    for num in nums:
        sub.append(abs(num-inp))

# 저장한 차들의 최대 공약수를 구함.
GCF = gcd(*sub)

# 순회하면서 약수를 구함.
ans = []
for num in range(1, int(GCF**0.5)+1):
    if num == 1:
        ans.append(GCF)
        continue
    if GCF % num == 0:
       ans.append(num)
       ans.append(GCF//num)

ans = list(set(ans))
ans.sort()
print(*ans)

"""
3
6
34
38

3
6 
10 
18

4
10
20
30
40
"""