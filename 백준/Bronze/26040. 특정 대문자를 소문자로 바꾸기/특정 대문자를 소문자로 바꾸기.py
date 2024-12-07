import sys

a=list(input())
b=list(input().split())

for i in range(len(a)):
    for k in range(len(b)):
        if a[i]==b[k]:
            a[i] = a[i].lower()
print(*a,sep="")