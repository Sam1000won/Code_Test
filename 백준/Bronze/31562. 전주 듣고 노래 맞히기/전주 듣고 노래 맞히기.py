N, M = map(int, input().split())
song = {}

for _ in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    A = [a1, a2, a3]	
    song[S] = A		

for _ in range(M):
    B = input().split()
    count = 0	
    title = ""

    for s in song:
        if B == song[s]:
            count += 1
            title = s

    if count >= 2:
        print("?")
    elif count == 1:
        print(title)
    else:
        print("!")