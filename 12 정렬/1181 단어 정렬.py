from sys import stdin
N = int(input())
words = list({stdin.readline().strip() for _ in range(N)})
words.sort(key = lambda x:(len(x), x))
print("\n".join(words))