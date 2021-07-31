N, K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

#예외처리
# if len(A) or len(B) > 6:
#     print(len(A),len(B))
#     print(N,"만큼 입력하시오")
#     exit()

B.sort(reverse=True)
A.sort()

for i in range(K):
    if A[i] < B[i]:
        A[i] , B[i] = B[i] , A[i]

result = 0

for i in A:
    result+=i

print(result)

