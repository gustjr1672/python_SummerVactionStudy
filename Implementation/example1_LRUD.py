#상하좌우
import time

N = int(input())
move = input().split()

start = time.time()
x = 1
y = 1

for m in move:
    if m == 'R' and x < N:
        x+=1
    elif m== 'L' and x > 1 :
        x-=1
    elif m == 'U' and y > 1:
        y-=1
    elif m == 'D' and y < N:
        y+=1

location = (y,x)
end = time.time()
print(location)
print(end - start)