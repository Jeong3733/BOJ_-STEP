from sys import stdin

N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(stdin.readline())] += 1

for elm in range(len(count)):
    if count[elm] > 0:
        for _ in range(count[elm]):
            print(elm)