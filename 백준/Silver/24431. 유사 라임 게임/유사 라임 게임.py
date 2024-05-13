from collections import defaultdict

A = int(input())

for i in range(A):
    dict = defaultdict(int)  # Initialize with default value 0 for counts
    res = 0
    L, F, M = map(int, input().split())
    arr = list(input().split())

    for j in arr:
        ending = j[-M:]
        dict[ending] += 1

    for j in dict:
        if dict[j] > 1:
            res += dict[j] // 2

    print(res)
