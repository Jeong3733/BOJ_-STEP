from sys import stdin, stdout

def MergeSort(List):
    # 기저 사례 : List의 길이가 1 이하일 때
    if len(List) <= 1:
        return List
    
    mid = len(List) // 2

    # 병합 정렬은 분할 정복 알고리즘의 한 종류로,
    # 재귀 호출을 통해서 리스트를 거의 동일한 크기의 2개의 리스트로 나누고
    # -> 분할(부분 배열로 나누기) (Divide)

    # 2개의 리스트를 순서에 맞게 병합하는 과정을 거친다.
    # -> 결합 (Merge)

    # List를 반으로 나누고, 재귀 호출을 통해서 정렬
    left_list = MergeSort(List[:mid])
    right_list = MergeSort(List[mid:])
    ret = Merge(left_list, right_list)

    return ret

def Merge(List1, List2):
    ret_list = []
    """ 
    내가 구현한 함수, 2751번 문제 통과 못함.
    remove 함수가 O(N)의 시간복잡도를 갖고 있기 때문인 듯 하다.

    while True:
        if List1[0] <= List2[0]:
            ret_list.append(List1[0])
            List1.remove(List1[0])
        else:
            ret_list.append(List2[0])
            List2.remove(List2[0])
        
        if len(List1) == 0:
            for i in List2:
                ret_list.append(i)
            break
        
        if len(List2) == 0:
            for i in List1:
                ret_list.append(i)
            break
    """
    i, j = 0, 0

    while i < len(List1) and j < len(List2):
        if List1[i] <= List2[j]:
            ret_list.append(List1[i])
            i += 1

        else:
            ret_list.append(List2[j])
            j += 1
    
    if i < len(List1):
        ret_list += List1[i:]
    if j < len(List2):
        ret_list += List2[j:]

    return ret_list

N = int(stdin.readline().strip())
List = [int(stdin.readline().strip()) for i in range(N)]
List = MergeSort(List)

"""
for element in List:
    stdout.write(str(element) + "\n")
"""
stdout.write("\n".join(map(str, List)))  