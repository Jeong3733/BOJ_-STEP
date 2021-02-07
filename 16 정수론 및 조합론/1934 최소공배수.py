def Euclid(a, b):
    big, small = max(a, b), min(a, b)
    if big % small == 0:
        return small
    return Euclid(small, big%small)

N = int(input())
ans = []
for _ in range(N):
    a, b = map(int, input().split())
    GCF = Euclid(a, b)
    ans.append(GCF * a//GCF * b//GCF)

print(*ans, sep="\n")

"""
3
1 45000
6 10
13 17
"""