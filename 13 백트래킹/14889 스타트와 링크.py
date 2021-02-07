from sys import stdin

# tmStart : 스타트 팀, player - tmStart = tmLink
def strNlink(tmStart):
    global ans

    # 기저 사례:
    if len(tmStart) == N/2:
        tmLink = [link for link in range(N) if link not in tmStart]
        stStart = 0; stLink = 0

        # zip 함수를 이용해서 하나의 for문에서 2개의 list를 동시에 접근 가능
        for col_s, col_l in zip(tmStart, tmLink):
            for row_s, row_l in zip(tmStart, tmLink):
                stStart += stat[col_s][row_s]
                stLink += stat[col_l][row_l]

        # print(abs(stStart - stLink), stStart, stLink, tmStart, tmLink)
        ans = min(ans, abs(stStart - stLink))
        return

    if tmStart:
        first = max(tmStart) + 1
    else:
        first = 0
    
    for picked in range(first, N):
        # 새로운 멤버
        tmStart.append(picked)
        strNlink(tmStart)
        tmStart.remove(picked)
    


N = int(input())
stat = [list(map(int, stdin.readline().split())) for _ in range(N)]
ans = 99999999
strNlink([])
print(ans)

"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
"""