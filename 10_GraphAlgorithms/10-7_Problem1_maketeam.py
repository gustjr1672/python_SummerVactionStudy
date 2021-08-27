def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input(). split())
parent = [0] * (n + 1)
answer = []

for i in range(0, n + 1):
    parent[i] = i

for i in range (m):
    oper, a, b = map(int, input(). split())

    if oper == 0:
     union_parent(parent, a, b)

    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            answer.append('YES')
        else:
            answer.append('NO')

for i in answer:
    print(i)