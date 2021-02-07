N, M = map(int, input().split())
chess_input = [list(input()) for i in range(N)]
cmp_ans = [[-1 for i in range(8)] for i in range(8)]

black = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
white = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

ans = 99999999

# height, width는 시작 위치(height부터 8칸, width부터 8칸씩 자름)
for height in range(N-8+1):
    for width in range(M-8+1):
        ans_black_first = 0
        ans_white_first = 0

        for index in range(8):
            # 잘라서 버퍼에 저장
            cmp_ans[index] = chess_input[height+index][width: width+8]

            # B로 시작했을 때와, W로 시작했을 때를 따로 나누어서 계산
            ans_black_first += [a == b for a, b in zip(black, cmp_ans[index]) if index % 2 == 0 ].count(False)
            ans_black_first += [a == b for a, b in zip(white, cmp_ans[index]) if index % 2 == 1 ].count(False)
            
            ans_white_first += [a == b for a, b in zip(white, cmp_ans[index]) if index % 2 == 0 ].count(False)                                   
            ans_white_first += [a == b for a, b in zip(black, cmp_ans[index]) if index % 2 == 1 ].count(False)

        # 가장 작은수 골라내는 과정
        if ans > min(ans_black_first, ans_white_first):
            ans = min(ans_black_first, ans_white_first)
print(ans)