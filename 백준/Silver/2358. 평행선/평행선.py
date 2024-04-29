import sys

# 입력 받기
n = int(sys.stdin.readline())
points = []

# x축과 y축에 대한 딕셔너리 초기화
x_axis = {}
y_axis = {}

# 점들을 받아서 x축과 y축에 따라 그룹화
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))
    if x in x_axis:
        x_axis[x] += 1
    else:
        x_axis[x] = 1
    
    if y in y_axis:
        y_axis[y] += 1
    else:
        y_axis[y] = 1

# x축과 y축에 평행한 직선의 개수 계산
parallel_lines = 0
for count in x_axis.values():
    if count > 1:
        parallel_lines += 1

for count in y_axis.values():
    if count > 1:
        parallel_lines += 1

# 결과 출력
print(parallel_lines)

