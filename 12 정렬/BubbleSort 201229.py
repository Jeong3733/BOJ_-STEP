def BubbleSort(List):

    # 한번 돌고 나면 가장 큰 원소가 맨 끝으로 이동하므로
    # 검사해야할 원소 수가 하나 감소함
    for sort_size in range(len(List), 1, -1):
        for index in range(sort_size-1):
            # 왼쪽게 크면 swap
            if List[index] > List[index+1]:
                List[index], List[index+1] = List[index+1], List[index]
    return List

N = int(input())
List = [int(input()) for i in range(N)]
BubbleSort(List)

for element in List:
    print(element)