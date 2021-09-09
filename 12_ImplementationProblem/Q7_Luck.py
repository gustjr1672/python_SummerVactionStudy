while(1):
    n =input()
    if len(n)%2 != 0:
        continue
    break

sum1 = 0
sum2 = 0

for i in range(len(n)):
    if i < len(n)//2:
        sum1 += int(n[i])
    else:
        sum2 += int(n[i])

if sum1 == sum2:
    print("LUCKY")

else:
    print("READY")
