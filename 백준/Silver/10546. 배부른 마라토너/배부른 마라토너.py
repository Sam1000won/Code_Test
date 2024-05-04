import sys
input = sys.stdin.readline

ple = int(input())
ple_dic = {}

for _ in range(ple):
    name = input().rstrip()
    if name not in ple_dic.keys():
        ple_dic[name] = 1
    else:
        ple_dic[name] += 1

for _ in range(ple - 1):
    name = input().rstrip()
    if name in ple_dic.keys():
        ple_dic[name] += 1

for key, value in ple_dic.items():
    if value % 2 == 1:
        print(key)
        break
