d=[0]*117

d[1]=1
d[2]=1
d[3]=1

n=int(input())

for i in range(4, n+1):
    d[i]=d[i-1]+d[i-3]

    
print(d[n])