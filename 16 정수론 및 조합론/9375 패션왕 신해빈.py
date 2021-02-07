import sys, collections

T = int(sys.stdin.readline())
answers = []

for _ in range(T):
    N = int(sys.stdin.readline())

    types = []
    for idx in range(N):
        name, type = sys.stdin.readline().rstrip().split()
        types.append(type)

    # howManyTypes, 각 종류의 개수.
    hMTypes = list(collections.Counter(types).values())

    tmp = 1
    for i in hMTypes:
        tmp *= (i + 1)

    answers.append(tmp-1)

print(*answers, sep="\n")

"""
3
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
11
hat headgear
a cloth
b cloth
c cloth
d cloth
e pants
f pants
g pants
h headgear
sunglasses eyewear
turban headgear
"""