def SelectionSort(List):
    for target in range(len(List)-1):
        least = target
        for index in range(target+1, len(List)):
            if List[least] > List[index]:
                least = index
        
        List[target], List[least] = List[least], List[target]

    return List

N = int(input())
List = [int(input()) for i in range(N)]
SelectionSort(List)

for element in List:
    print(element)