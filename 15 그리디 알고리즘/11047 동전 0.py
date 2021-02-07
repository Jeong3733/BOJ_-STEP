import sys
N, K = map(int, input().split())
tmp = K

coin = [int(sys.stdin.readline()) for _ in range(N)]

ret = 0
for idx in list(reversed(coin)):
    ret += tmp // idx
    tmp = tmp % idx

print(ret)

"""
10 4200
1
5
10 
50
100
500
1000
5000
10000
50000

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
"""