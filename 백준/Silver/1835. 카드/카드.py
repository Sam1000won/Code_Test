from collections import deque

n = int(input())
d = deque()
d.append(n)

for i in range(n-1, 0, -1):
    d.appendleft(i)
    for j in range(i):
        d.appendleft(d.pop())

print(*d)