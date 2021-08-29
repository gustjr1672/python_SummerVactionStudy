#주어진 수들을 M번 더하여 가장 큰 수를 만든다
#같은 숫자가 K번을 초과해서 더해질 수 없다

import time

N,M,K = map(int, input().split())
max, max2, sum = 0, 0 ,0

# array = [N]
array = list(map(int,input().split()))
# array = [int(x) for x in array]

start = time.time()


# array.sort()
# first = array[N-1]
# second = array[N-2]
#
# result = 0
#
# while(M != 0):
#     for _ in range(K):
#         if M==0:
#             break
#         result +=first
#         M-=1
#
#     if M==0:
#         break
#     result+= second
#     M-=1
#
# end = time.time()
# print(result)


#수학 공식을 이용해서 푸는 방법
array.sort()
first = array[N-1]
second = array[N-2]

count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
result += count * first
result += (M-count) * second

end = time.time()
print(result)


#sort()를 사용해서 크기 순으로 정렬했으면, 쉽게 풀 수 있었다.
#while문 수정