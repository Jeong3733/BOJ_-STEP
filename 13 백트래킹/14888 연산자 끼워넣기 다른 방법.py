import sys
def bck_trk(idx, tmp, add, sub, mul, div):
    if idx == N:
        maxv = max(maxv, tmp)
        minv = min(minv, tmp)

    if add > 0:
        bck_trk(idx+1, tmp+num[idx], add-1, sub, mul, div)
    if sub > 0:
        bck_trk(idx+1, tmp-num[idx], add, sub-1, mul, div)
    if mul > 0:
        bck_trk(idx+1, tmp*num[idx], add, sub, mul-1, div)
    if div > 0:
        bck_trk(idx+1, int(tmp/num[idx]), add, sub, mul, div-1)

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
maxv = -sys.maxsize
minv = sys.maxsize
    
bck_trk(1, num[0], op[0], op[1], op[2], op[3])
print(maxv, minv, sep = "\n")