import sys

N = input()

for num in range(int(N)):
    num_list = list(map(int, str(num)))
    ret = sum(num_list) + num

    if ret == int(N):
        print(num)
        sys.exit()

print(0)