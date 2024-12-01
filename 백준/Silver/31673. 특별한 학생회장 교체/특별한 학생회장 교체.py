import sys
put = sys.stdin.readline

N, M = map(int, put().split())
V = sorted(list(map(int, put().split())), reverse=True)
v = sum(V) / 2

for i in range(N):
    v -= V[i]
    if v <= 0:
        m = i + 2
        break
else:
    m = N + 1

print(M // m)
