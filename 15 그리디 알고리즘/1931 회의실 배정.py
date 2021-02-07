import sys

N = int(input())
time = [[-1] * 2 for _ in range(N)]

for i in range(N):
    time[i][0], time[i][1] = map(int, sys.stdin.readline().strip().split())

time.sort(key=lambda x:(x[1], x[0]))    

ret, nowE = 0, 0
for start, end in time:
    if nowE <= start:
        nowE = end
        ret += 1
        
print(ret)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""