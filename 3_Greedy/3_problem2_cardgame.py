import numpy

N, M = map(int, input().split())
array = []

#행렬 만들기
for _ in range(N):
        tem = list(map(int,input().split()))
        array.append(tem)

result = []

#1열 씩 살펴보기
for i in range(N):
        min = 0
        for j in range(M):   #행을 옮겨가며 가장 작은 수 찾기
                min = array[i][0]
                line = i
                if min > array[i][j] and line == i:
                        min = array[i][j]
                        result.append(min)
result.sort()
print(result[N-1])

#한 줄을 입력 받을때마다, 그 줄에서 가장 작은 값을 찾는 방법이 있다.
#min(array) 라는 함수를 사용하면, list내에서 가장 작은 값을 바로 찾을 수 있다.