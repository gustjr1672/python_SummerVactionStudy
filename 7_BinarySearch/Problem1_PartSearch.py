def search_part(array, target, N, M, answer):
    wrong = 0
    for i in range(M+1):
        for j in range(N+1):
            if array[j] == target[i]:
                answer.append("yes")

            elif array[j] != target[i]:
                wrong +=1
                if wrong == N+1:
                    answer.append("no")

N = int(input())
array = list(map(int, input().split()))

M= int(input())
target = list(map(int, input().split()))

answer = []

search_part(array, target, N-1, M-1, answer)

for i in answer:
    print(i, end= " ")