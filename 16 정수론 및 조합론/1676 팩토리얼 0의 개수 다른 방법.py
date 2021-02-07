# https://shoark7.github.io/programming/algorithm/number-of-trailing-zeros-in-factorial
# https://ksj14.tistory.com/entry/BackJoon1676-%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-0%EC%9D%98-%EA%B0%9C%EC%88%98

def getTrailingZeroes(n):
    two, five = 0, 0
    
    i = 2
    while i <= n:
        two += n // i
        i = i*2

    i = 5
    while i <= n:
        five += n // i
        i = i*5

    return two, five

N = int(input())
print(min(getTrailingZeroes(N)))