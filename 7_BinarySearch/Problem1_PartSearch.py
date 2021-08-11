import time

def search_part(array, target, N, M, answer):
    for i in range(M):
        wrong = 0
        for j in range(N):
            if array[j] == target[i]:
                answer.append("yes")

            elif array[j] != target[i]:
                wrong +=1
                if wrong == N:
                    answer.append("no")

N = int(input())
array = list(map(int, input().split()))

M= int(input())
target = list(map(int, input().split()))

start = time.time()

answer = []

search_part(array, target, N, M, answer)

for i in answer:
    print(i, end= " ")

end = time.time()
print(start -end)