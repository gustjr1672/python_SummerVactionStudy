#거슬러 줘야할 동전의 최소 개수를 구하라.

n = int(input())  #거슬러 줘야하는 돈
count = 0

coinlist = [500, 100, 50, 10]

for coin in coinlist:
    count += n // coin
    n %= coin

print(count)
