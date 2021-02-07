N = int(input())
P = list(reversed(sorted(list(map(int, input().split())))))

ret = 0
for idx in range(len(P)):
    ret += P[idx] * (idx+1)
print(ret)

"""
5
3 1 4 3 2
"""