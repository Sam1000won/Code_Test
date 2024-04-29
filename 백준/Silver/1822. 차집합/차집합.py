a, b = map(int,input().split())
A, B = {},{}
for n in map(int,input().split()):
	A[n] = 1
for n in map(int,input().split()):
	B[n] = 1

C = []
for i in A:
	if i not in B:
		C += [i]
print(len(C))
print(*sorted(C))