n,m = map(int,input().split())
pipe = list(map(int,input().split()))
pipe.sort()

start = pipe[0]
count = 1

for i in pipe[1:]:
    if (i+0.5)-(start-0.5)<=m:
        continue
    else:
        start = i
        count+=1
print(count)