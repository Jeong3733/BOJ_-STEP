from sys import stdin

def w(a, b, c):
    # 첫번째 조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1    

    # 두번째 조건
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)


    if cache[a][b][c] != None:
        return cache[a][b][c]


    # 세번째 조건
    if a < b and b < c:
        cache[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return cache[a][b][c]

    # 마지막 조건(else)
    cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)        
    return cache[a][b][c]
    

# cache = [[[None]*21]*21]*21
cache = [[[None]*21 for i in range(21)] for i in range(21)]

ans = ""

while(True):
    a, b, c = map(int, stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break

    ans += "w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(w(a, b, c)) + "\n"

print(ans)

"""
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
"""