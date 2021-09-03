n, m = map(int, input().split())
ball = list(map(int,input().split()))

result = 0

for i in range(n):
    for j in range(n):
        if ball[i] != ball[j] and i < j:
            result += 1

print(result)