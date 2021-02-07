cache = [[[None]*2]*2]*2
cache2 = [[[None]*2 for i in range(2)] for i in range(2)]
cache3 = [[[None] for i in range(2) for i in range(2)] for i in range(2)]

print(id(cache))
print(id(cache2))
print(id(cache3))

for k in range(2):
    for j in range(2):
        for i in range(2):
            print(k, j, i, id(cache[k][j][i]), id(cache2[k][j][i]))
            print(k, j, i, id(cache[k][j]), id(cache2[k][j]))
            print(k, j, i, id(cache[k]), id(cache2[k]))
            print()

cache[0][0][0] = 1
cache2[0][0][0] = 1
cache3[0][0][0] = 1

print(cache)
print(cache2)
print(cache3)