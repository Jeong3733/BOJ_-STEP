from sys import stdin

N = int(input())

arr = []

for _ in range(N):
    age, name = stdin.readline().split()
    arr.append((int(age), name))

arr = sorted(arr, key = lambda x:x[0])

for age, name in arr:
    print(age, name)