def QuickSort(List):
    # 기저 사례 : 리스트 크기가 1보다 작을 때
    if len(List) <= 1:
        return List

    # 퀵 정렬은 분할 정복 알고리즘의 한 종류로,
    # 피벗을 정하고 피벗보다 큰 리스트, 작은 리스트로 나눈 뒤,
    # -> 분할(부분 배열로 나누기) (Divide)

    # 나눈 리스트들을 병합하는 과정을 거친다.
    # -> 결합 (Merge)
    
    # 피벗보다 작은 것, 큰 것, 같은 것을 저장할 리스트
    small, big, equal = [], [], []

    # 피벗 정함
    pivot = List[len(List) // 2]

    # 피벗을 기준으로 큰 것, 작은 것 나눔
    for element in List:
        if element > pivot:
            big.append(element)
        elif element < pivot:
            small.append(element)
        else:
            equal.append(element)

    # 재귀를 통해서 작은 리스트, 큰 리스트를 정렬 후 병합하고 종료
    ret = QuickSort(small) + equal + QuickSort(big)
    return ret

N = int(input())
List = [int(input()) for i in range(N)]
List = QuickSort(List)

for element in List:
    print(element)