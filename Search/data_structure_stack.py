#stack은 선입후출(FILO)
#stack은 라이브러리 없이 사용가능 (list에서 append, pop사용)
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
stack = stack[::-1]
print(stack)
