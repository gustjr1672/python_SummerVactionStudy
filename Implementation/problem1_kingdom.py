import  re
import time

row = ['1','2','3','4','5','6','7','8']
colum = ['a','b','c','d','e','f','g','h']
move = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 숫자와 문자 (행과 열)을 분리한다 .
#ex) a1 을 a와 1로 분리한다.
location = input()

stat = time.time()

now_colum =re.search('[a-z]' ,location).group() #열을 분리한다. #group 은 매치된 문자열을 리턴함
now_row = re.search('[0-9]',location).group() #행을 분리한다.

count = 0

#  현재위치 (x,y) 좌표 찾기 (인덱스 찾기)
for i in range(len(colum)):
    if now_colum == colum[i]:
        x = i+1
    if now_row == row[i]:
        y = i+1

for m in move:
    move_colum = x + m[0]
    move_row = y + m[1]

    if move_colum > 0 and move_colum < 9 and move_row > 0 and move_row < 9:
        count+=1

end = time.time()
print(count)
print(end - stat)








