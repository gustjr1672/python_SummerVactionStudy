import time

N = int(input())

array = []
for _ in range(N):
    array.append(input())

start = time.time()

array.sorted(array,revere = True)
end= time.time()

for i in range(len(array)):
    print(array[i],end=' ')

print("\n",end-start)