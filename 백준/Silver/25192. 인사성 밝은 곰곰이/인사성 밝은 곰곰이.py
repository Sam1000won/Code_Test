import sys

input_func = sys.stdin.readline

n = int(input_func())
name = set()
count = 0

for _ in range(n):
    user = input_func().strip()
    if user == 'ENTER':
        count += len(name)
        name = set()
    else:
        name.add(user)

count += len(name)
print(count)
