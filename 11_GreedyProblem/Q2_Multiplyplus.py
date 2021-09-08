s = input()
result = 1


for i in range(len(s)):
    if int(s[i]) == 0 and i == 0:
        result = ( int(s[i]) + int(s[i+1]) ) // int(s[i+1])
    if s[i] == 1:

    if int(s[i]) != 0:
        result *= int(s[i])


print(result)
#
# #i == 1일때
# 이거 하나 추가하면 돼
# 그리고 맨처음 or result값이 0일 땐 모든 수 다 더해줘야돼
# 맨처음엔 result값이 0이고
