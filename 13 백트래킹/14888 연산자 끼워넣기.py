from itertools import permutations

def insert_op(index, op, value):
    if index == N-1:
        ans.append(value)
        # print(value, op, end="\n")
        return

    ret = 0
    tmp = nums[index + 1]

    # 덧셈
    if op[index] == 0:
        ret = value + tmp

    # 뺄셈
    elif op[index] == 1:
        ret = value - tmp

    # 곱셈
    elif op[index] == 2:
        ret = value * tmp

    # 나눗셈
    elif op[index] == 3:
        ret = abs(value) // abs(tmp)

        if value < 0 or tmp < 0:
            ret *= -1

    # print(value, tmp, ret, end="   ")
    insert_op(index+1, op, ret)
    

N = int(input())
nums = list(map(int, input().split()))

# 0: "+", 1: "-", 2: "*", 3: "//"
opArr = []
opCount = list(map(int, input().split()))
for i in range(4):
    opArr += [i] * opCount[i]

ans = []

for opCase in set(permutations(opArr, N-1)):
    insert_op(0, opCase, nums[0])

print(max(ans), min(ans), sep="\n")

"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
"""