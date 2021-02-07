# 알고리즘 문제 해결 전략 149p
# nums에서 3개를 고르는 모든 조합을 찾은 뒤,
# 원소들의 합 중에서 M보다 작으면서 가장 큰 수를 찾는 함수

# *** 각 함수에서 하나의 원소를 고른 뒤, 재귀호출로 나머지 원소 고름 ***

# lis : 지금까지 고른 원소
def black(lis):
    global M, nums, biggest 

    # 기저 사례 : lis의 크기가 3일 때
    if len(lis) == 3:
        # M보다 작으면서 가장 큰 수인지 판단
        if sum(lis) >= biggest and sum(lis) <= M:
            biggest = sum(lis)
        return

    # 가장 최근에 고른 수의 (lis의 마지막 원소 == lis[-1]) 
    # nums상 위치(index)를 구한 뒤, (nums.index(마지막 원소))
    # nums에서 그 이후의 수들로 (nums[마지막 원소의 위치+1 : ]) list를 생성
    if(lis):
        PartOfNums = nums[nums.index(lis[-1]) + 1:]
    else:
        PartOfNums = nums[:-2]

    # 원소 하나를 고르는 작업
    for i in PartOfNums:
        lis.append(i)
        black(lis)
        lis.pop()

    return


N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
biggest = 0; lis = []

black(lis)
print(biggest)