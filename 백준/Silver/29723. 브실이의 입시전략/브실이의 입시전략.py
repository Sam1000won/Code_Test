K, M, N = map(int, input().split())
point = {}

for _ in range(K):
    school, poin = input().split()
    point[school] = int(poin)

open_point = 0
deleted_keys = []

for _ in range(N):
    t = input()
    open_point += point[t]
    deleted_keys.append(t)

for key in deleted_keys:
    del point[key]

point = sorted(point.items(), key=lambda x: x[1])

min_point, max_point = 0, 0

for i in range(M - N):
    min_point += point[i][1]
    max_point += point[-i - 1][1]

print(open_point + min_point, open_point + max_point)
