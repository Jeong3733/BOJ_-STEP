a, b = map(int, input().split())

GCF, LCM = 0, 0

for i in range(1, min(a, b)+1):
    if a%i == 0 and b%i == 0 and i > GCF:
        GCF = i

LCM = GCF * (a//GCF) * (b//GCF)
print(GCF, LCM, sep="\n")