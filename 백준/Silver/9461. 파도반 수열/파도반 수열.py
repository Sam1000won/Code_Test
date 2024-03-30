import sys
input = sys.stdin.readline
arr = [0, 1, 1, 1] + [0 for x in range(97)]

def func(x):
  if arr[x]:
    return arr[x]
  else:
    arr[x] = func(x-2) + func(x-3)
    return arr[x]

t = int(input())
for _ in range(t):
  n = int(input())
  print(func(n))