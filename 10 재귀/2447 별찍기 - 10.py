# y, x는 별찍기를 시작할 좌표, n은 판의 크기
def star(arr, n, x, y):

    # 기저 사례 : n==3일 때, 더 이상 쪼개지지 않음.
    if n == 3:
        for j in range(3):
            for i in range(3):
                if j == 1 and i == 1:
                    continue
                arr[y+j][x+i] = "*"
        return
    
    # n이 9이상일 때, 주어진 판을 9등분해서 재귀 호출
    
    # "크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다"
    # ==  N/3의 패턴을 8개 사용

    # 중앙에 있는 칸 비워둠

    for j in range(3):
        for i in range(3):
            dy = (n*j) // 3
            dx = (n*i) // 3

            # 중앙
            if j == 1 and i == 1:
                continue
            
            # 재귀호출
            else:
                star(arr, n // 3, y + dy, x + dx)
    return

if __name__ == "__main__":
    N = int(input())
    arr = [[" " for i in range(N)] for i in range(N)]
    star(arr, N, 0, 0)
    for j in range(N):
        for i in range(N):
            print(arr[j][i], end="")
        print()
        