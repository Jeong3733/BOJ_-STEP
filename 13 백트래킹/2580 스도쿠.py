from sys import stdin

def bck_trk(t):
    if t == len(zero):
        return True

    y = zero[t][0]
    x = zero[t][1]

    for i in range(1, 10):
        if test(y, x, i):
            sdk[y][x] = i
            if bck_trk(t+1):
                return True
        sdk[y][x] = 0
    return False

 

def test(y, x, num):
    # 가로줄 체크
    if num in sdk[y]:
        return False
    # 세로줄 체크
    for j in range(9):
        if num == sdk[j][x]:
            return False
    # 3X3 영역 체크
    for j in range(y-y%3, y-y%3+3):
        for i in range(x-x%3, x-x%3+3):
            if num == sdk[j][i]:
                return False
    return True

sdk = [list(map(int, stdin.readline().split())) for _ in range(9)]

zero = [(j, i) for j in range(9) for i in range(9) if sdk[j][i] == 0]    

bck_trk(0)

for j in range(9):
    for i in range(9):
        print(sdk[j][i], end = " ")
    print()


"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""