string = []
while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break

    if b > a and b % a == 0:
        string.append("factor")
    elif a > b and a % b == 0:
        string.append("multiple")
    else:
        string.append("neither")

    

print(*string, sep="\n")

"""
8 16
32 4
17 5
0 0
"""