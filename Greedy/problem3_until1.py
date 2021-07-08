N, K = map(int,input().split())


result = 0
count = 0
while(N!=0):
        if N%K ==0:
                while(N%K == 0):
                        N= N/K
                        count +=1
                        print("나누기")
        else:
                while(N%K != 0):
                        N -= 1
                        count +=1
                        print("빼기")
if N==0:
        count-=1
print(count)


