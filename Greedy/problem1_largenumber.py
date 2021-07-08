import time

N,M,K = map(int, input().split())
max, max2, sum = 0, 0 , 0

array = [N]
array = input().split()
array = [int(x) for x in array]

start = time.time()
#가장 큰 수 찾기
for i in range(len(array)):
    if max < array[i]:
        max =  array[i]

#두 번째로 큰 수 찾기
for j in range(len(array)):
    if max2 < array[j] and array[j] != max:
        max2 = array[j]

#가장 큰 수 k번 두 번째 큰 수 1번 더하기
while M != 0:
    for _ in range(K):
        sum += max
        M -= 1
    sum += max2
    M-=1
end = time.time()

print(sum)
print(end - start)

#sort()를 사용해서 크기 순으로 정렬했으면, 쉽게 풀 수 있었다.