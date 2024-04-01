import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [tuple(map(int, input().split())) for _ in range(n)]

	# x y별로 분리할 dict 초기화
    grouped_data_x = {}
    grouped_data_y = {}

	# dict에 데이터 삽입
    for x, y in nums:
        grouped_data_x.setdefault(x, []).append(y)
        grouped_data_y.setdefault(y, []).append(x)

	# 최종 길이를 반환할 결과값 초기화
    res = 0

	# dict에서 values값을 가져와 for문 실행
    for x_coords in grouped_data_x.values():
        x_coords.sort() # 정렬하지 않으면 음수 값이 나올 수 있음 ex [1,2]
        for i in range(len(x_coords) - 1, 0, -2): # 인접한 쌍으로 길이 계산 후 추가
            res += x_coords[i] - x_coords[i - 1]

	# dict에서 values값을 가져와 for문 실행
    for y_coords in grouped_data_y.values():
        y_coords.sort() # 정렬하지 않으면 음수 값이 나올 수 있음 ex [1,2]
        for i in range(len(y_coords) - 1, 0, -2): # 인접한 쌍으로 길이 계산 후 추가
            res += y_coords[i] - y_coords[i - 1]

	# 결과값 출력
    print(res)