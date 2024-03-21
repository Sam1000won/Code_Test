n = int(input())
li = list(map(int,input().split()))
li.sort()
 
s = 0
tm = []
for i in li:
    s += i
    tm.append(s)
print(sum(tm))