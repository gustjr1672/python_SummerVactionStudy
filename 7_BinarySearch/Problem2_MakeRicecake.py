import time

N , M = map(int,input().split())
array = list(map(int,input().split()))

start = time.time()
array.sort(reverse=True)
print(array)
#가장 긴 떡의 길이가 h가 됨
h = array[0]
count = 0

while(count <= M):
    for i in range(N):
        if array[i] - h > 0:
            count += array[i] - h
            print(h)
        if array[i] - h <= 0 and count <= M:
            h-=1


end = time.time()
print(h)
print(end - start)