n = int(input())
adven = list(map(int, input().split()))

#내림차순으로 정렬
adven.sort()

#가장 큰 수 저장
min = adven[0]
result = 0

while(n != 0):
    # 가장 큰 수만큼 전체에서 뺀다
    n-= max
    # 1개의 group이 만들어 졌다
    result+=1
    # 3 2 2 2 1중에 3번째 인덱스가 다음으로 가장 큰 수가 된다.
    max = adven[max]

print(result)

