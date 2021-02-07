a = input().split('-')
num = []

for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

for i in range(0, len(num)-1):
    num[i+1] = num[i] - num[i+1]

print(num[-1])