s = input()

count0 = 0
count1 = 0
result = 0



if s[0] == '0':
    count0+=1
else:
    count1 +=1

for i in range(len(s)-1):
    if count0 > count1:
        if s[i] != s[i+1]:
            result +=1

    if count0 < count1:
        if s[i] != s[i+1]:
            result+=1

print(result)
