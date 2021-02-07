from math import gcd

N = int(input())
num = list(map(int, input().split()))
ans = ""

for n in num:
    if n == num[0]:
        continue
    GCF = gcd(num[0], n)
    ans += str(num[0]//GCF) + "/" + str(n//GCF) + "\n"

print(ans.rstrip())