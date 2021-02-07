import sys

N = input()

for i in range(int(N)):
    forSum = str(i)
    ret = int(i)
    for j in forSum:
        ret += int(j)

    if ret == int(N):
        print(i)
        sys.exit()

print(0)