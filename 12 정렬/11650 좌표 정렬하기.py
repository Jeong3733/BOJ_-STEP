N = int(input())

dic = []
for _ in range(N):
    x, y = map(int, input().split())
    dic.append((x, y))

for x, y in sorted(dic):
    print(x, y)
