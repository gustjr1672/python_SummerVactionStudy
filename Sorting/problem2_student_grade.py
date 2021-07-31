N = int(input())

def setting(data):
    return data[1]

array = []

for _ in range(N):
    array.append(input().split())

array = sorted(array,key = setting)  #lamda를 써서도 가능

for i in range(len(array)):
    print(array[i][0], end =' ')
