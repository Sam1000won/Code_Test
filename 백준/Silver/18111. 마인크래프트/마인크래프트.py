import sys

N, M, B = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = sys.maxsize
idx = 0

for floor in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(N):
        for j in range(M):

            if field[i][j] > floor :
                exceed_block += field[i][j] - floor
            else : 
                lack_block += floor - field[i][j]

    if exceed_block + B >= lack_block :
        if (exceed_block * 2) + lack_block <= answer:
            answer = (exceed_block * 2) + lack_block
            idx = floor


print(answer, idx)