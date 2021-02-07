def InsertionSort(List):
    # target은 미리 정렬된 리스트와 비교할 원소
    # check은 정렬된 리스트 안에서 target과 비교하는 원소의 index
    # 바깥쪽 for문은 미리 정렬된 list에 끼워넣을 target을 선택,
    # 안쪽 for문은 target의 적절한 위치를 찾기 위해서 target 앞 쪽의 index를 여러개 비교해봄.


    # target을 정하는 바깥쪽 for문
    # 적절한 위치를 찾기 위해서 사용할 check(index)
    for trg_index in range(1, len(List)):
        target = List[trg_index]
        check = trg_index-1

        # check를 1씩 감소해가며 target과 비교함
        while check >=0 and List[check] > target:
            List[check+1] = List[check]
            check -= 1
        List[check+1] = target

    return List

N = int(input())
List = [int(input()) for i in range(N)]
InsertionSort(List)

for element in List:
    print(element)