def CountingSort(List, count):
    # count의 index는 정렬할 배열들의 값, value는 그 값들이 나온 횟수
    # 각각 요소가 얼마나 나왔는지 세기
    for elm in List:
        count[elm] += 1
    
    # value를 누적 시킨 것을 계산하기
    for index in range(1, len(count)):
        count[index] += count[index-1]

    # ret = [-1 for _ in range(len(List))]

    # 위보다 아래처럼 하는 게 더 가독성이 좋은듯
    ret = [-1] * len(List)

    # count 리스트를 통해서 정렬
    for index in reversed(range(len(List))):
        count[List[index]] -= 1
        ret[count[List[index]]] = List[index]

    return ret


N = int(input())
List = [int(input()) for _ in range(N)]
count = [0] * (max(List)+1)

List = CountingSort(List, count)

for elm in List:
    print(elm)