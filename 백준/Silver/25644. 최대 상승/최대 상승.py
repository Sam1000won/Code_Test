import sys
input = sys.stdin.readline

day = int(input())
ANA = list(map(int, input().split()))
ben, res = 0, 0

for i in range(day-1, -1, -1):
    ben = max(ben, ANA[i])
    res = max(res, ben - ANA[i])

print(res)