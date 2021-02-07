import sys

sys.setrecursionlimit(10**9)

def LCS(idx1, idx2):
    if idx1 >= len(str1) or idx2 >= len(str2):
        return 0

    if cache[idx1][idx2] != -1:
        return cache[idx1][idx2]

    if str1[idx1] == str2[idx2]:
        ret = 1+LCS(idx1+1, idx2+1)
    else:
        ret = max(LCS(idx1+1, idx2), LCS(idx1, idx2+1))

    cache[idx1][idx2] = ret
    return cache[idx1][idx2]

str1, str2 = sys.stdin.readline().strip(), sys.stdin.readline().strip()
cache = [[-1]*len(str2) for _ in range(len(str1))]

print(LCS(0, 0))       

"""
ACAYKP
CAPCAK
"""