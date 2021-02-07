N = int(input())

dic = []
for _ in range(N):
    x, y = map(int, input().split())
    dic.append((x, y))

for x, y in sorted(dic, key = lambda x:(x[1], x[0])):
    print(x, y)
