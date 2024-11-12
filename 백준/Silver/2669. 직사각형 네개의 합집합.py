'''
문제 
평면에 네 개의 직사각형이 놓여 있는데 그 밑변은 모두 가로축에 평행하다. 이 네 개의 직사각형들은 서로 떨어져 있을 수도 있고, 겹쳐 있을 수도 있고, 하나가 다른 하나를 포함할 수도 있으며, 변이나 꼭짓점이 겹칠 수도 있다.

이 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오.

입력
입력은 네 줄이며, 각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다. 첫 번째와 두 번째의 정수는 사각형의 왼쪽 아래 꼭짓점의 x좌표, y좌표이고 세 번째와 네 번째의 정수는 사각형의 오른쪽 위 꼭짓점의 x좌표, y좌표이다. 모든 x좌표와 y좌표는 1이상이고 100이하인 정수이다.

출력
첫 줄에 네개의 직사각형이 차지하는 면적을 출력한다.

예제 입력
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6

예제 출력
26
'''

# 문제 해결 방법
'''
2 가지를 생각을 했다.

첫번째 : 면적 계산 후 중복된 부분 빼기
  방법: 각 사각형의 면적을 계산한 후, 겹치는 부분을 찾아서 면적에서 빼는 방식입니다.
  수식: 각 사각형의 면적은 ( (x2 - x1) \times (y2 - y1) )로 계산합니다.
  장점: 간단하게 면적을 계산할 수 있으며, 겹치는 부분을 정확하게 빼면 됩니다.
  단점: 겹치는 부분을 찾는 것이 복잡할 수 있으며, 특히 사각형의 수가 많아질수록 계산량이 증가합니다.

# 첫번째 코드
def calculate_area(rectangles):
    # 각 직사각형의 면적 계산
    total_area = 0
    for x1, y1, x2, y2 in rectangles:
        total_area += (x2 - x1) * (y2 - y1)

    # 중복 면적 계산
    overlap_area = 0
    n = len(rectangles)

    # 모든 쌍의 직사각형에 대해 중복 면적 계산
    for i in range(n):
        for j in range(i + 1, n):
            overlap_area += calculate_overlap(rectangles[i], rectangles[j])

    return total_area - overlap_area

def calculate_overlap(rect1, rect2):
    # 두 직사각형의 겹치는 부분을 계산
    x1 = max(rect1[0], rect2[0])  # 겹치는 x1
    y1 = max(rect1[1], rect2[1])  # 겹치는 y1
    x2 = min(rect1[2], rect2[2])  # 겹치는 x2
    y2 = min(rect1[3], rect2[3])  # 겹치는 y2

    # 겹치는 부분이 유효한지 확인
    if x1 < x2 and y1 < y2:  # 겹치는 면적이 존재하는 경우
        return (x2 - x1) * (y2 - y1)
    return 0  # 겹치는 부분이 없으면 0 반환

if __name__ == "__main__":
    rectangles = []
    for i in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))
    
    result = calculate_area(rectangles)
    print(result)
  
  # 결과값 25

두번째 : 좌표를 기준으로 계산하기
  방법: 모든 사각형의 좌표를 기준으로 계산하고, 겹치지 않는 부분을 따로 계산하는 방식입니다.
  장점: 사각형의 좌표를 정리한 후, 겹치는 부분을 쉽게 처리할 수 있습니다. 특히 좌표를 정렬한 후에 겹치는 부분을 효율적으로 찾아낼 수 있습니다.
  단점: 초기화하고 처리하는 과정이 다소 복잡할 수 있으며, 좌표를 정리하는 데 시간이 소요될 수 있습니다.

# 두번째 코드
def calculate_area(rectangles):
    # 각 직사각형의 면적 계산
    total_area = 0
    for x1, y1, x2, y2 in rectangles:
        total_area += (x2 - x1) * (y2 - y1)

    # 중복 면적 계산
    overlap_area = 0
    n = len(rectangles)

    # 모든 쌍의 직사각형에 대해 중복 면적 계산
    for i in range(n):
        for j in range(i + 1, n):
            overlap_area += calculate_overlap(rectangles[i], rectangles[j])

    return total_area - overlap_area

def calculate_overlap(rect1, rect2):
    # 두 직사각형의 겹치는 부분을 계산
    x1 = max(rect1[0], rect2[0])  # 겹치는 x1
    y1 = max(rect1[1], rect2[1])  # 겹치는 y1
    x2 = min(rect1[2], rect2[2])  # 겹치는 x2
    y2 = min(rect1[3], rect2[3])  # 겹치는 y2

    # 겹치는 부분이 유효한지 확인
    if x1 < x2 and y1 < y2:  # 겹치는 면적이 존재하는 경우
        return (x2 - x1) * (y2 - y1)
    return 0  # 겹치는 부분이 없으면 0 반환

if __name__ == "__main__":
    rectangles = []
    for i in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))
    
    result = calculate_area(rectangles)
    print(result)

'''
# 정답
'''
100*100 배열을 만들어서 사각형이 있는 부분을 1로 생성하여 마지막 배열에서 총 1의 갯수를 계산.
시간 복잡도 (o^2) 값이 커질수록 성능이 많이 떨어진다.
'''
''' 정답 1 코드드
def solution(rectangles):
    # 101x101 크기의 배열 초기화 (0~100까지 포함)
    grid = [[0] * 101 for _ in range(101)]

    # 각 직사각형의 면적을 grid에 표시
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x][y] = 1  # 해당 좌표에 1을 추가

    # 전체 면적 계산
    total_area = 0
    for x in range(101):
        for y in range(101):
            total_area += grid[x][y]  # 1인 부분의 개수를 세기

    return total_area

if __name__ == "__main__":
    li = []
    for i in range(4):
        x,y,z,e = map(int,input().split())
        li.append((x,y,z,e))
    print(solution(li))
'''
'''
스위핑 알고리즘을 사용한 방법

1 .이벤트 포인트 생성: 각 직사각형의 시작점과 끝점을 이벤트로 추가합니다. 시작점은 활성화된 상태로, 끝점은 비활성화된 상태로 처리.
2. 이벤트 정렬: x좌표를 기준으로 이벤트를 정렬하여 순차적으로 처리할 수 있도록 함
3. 활성 구간 관리: 현재 활성화된 y좌표 범위를 리스트로 관리합니다. calculate_y_length 함수는 이러한 범위에서 총 길이를 계산
4. 면적 계산: 각 이벤트를 처리하면서 x좌표의 변화에 따른 면적을 계산합니다. 이전 x좌표와 현재 x좌표 사이의 폭과 현재 활성화된 y좌표 범위의 길이를 곱하여 면적을 누적
5 .활성 구간 업데이트: 시작점일 경우 y좌표 범위를 추가하고, 끝점일 경우 해당 범위를 제거

'''
# 정답 2 코드
def calculate_area(rectangles):
    events = []  # 이벤트 포인트를 저장할 리스트 초기화
    
    # 각 직사각형의 이벤트 포인트 생성
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))  # 시작점 이벤트: (x1, y1, y2, 1)
        events.append((x2, y1, y2, -1))  # 끝점 이벤트: (x2, y1, y2, -1)

    # 이벤트 포인트를 x좌표 기준으로 정렬
    events.sort()

    # 현재 활성화된 y좌표 범위를 관리할 리스트
    active_intervals = []
    last_x = 0  # 이전 x좌표를 저장하기 위한 변수
    total_area = 0  # 총 면적을 저장할 변수

    def calculate_y_length(intervals):
        # 주어진 y좌표 범위에서의 총 길이를 계산
        if not intervals:
            return 0  # 활성 구간이 없으면 길이는 0
        
        intervals.sort()  # y좌표 범위를 정렬
        total_length = 0  # 총 길이를 저장할 변수
        current_start, current_end = intervals[0]  # 첫 번째 범위를 초기화

        # 나머지 범위를 순회하며 총 길이 계산
        for start, end in intervals[1:]:
            if start > current_end:  # 비활성 구간일 경우
                total_length += current_end - current_start  # 현재 범위의 길이를 추가
                current_start, current_end = start, end  # 현재 범위를 업데이트
            else:  # 겹치는 구간일 경우
                current_end = max(current_end, end)  # 최대 끝점을 업데이트

        total_length += current_end - current_start  # 마지막 범위의 길이를 추가
        return total_length  # 총 길이 반환

    # 이벤트 처리
    for x, y1, y2, typ in events:
        # 면적 계산
        if last_x != 0:  # 첫 번째 이벤트가 아닐 경우
            width = x - last_x  # x좌표 변화량 (현재 x - 이전 x)
            height = calculate_y_length(active_intervals)  # 활성 y좌표 범위의 총 길이
            total_area += width * height  # 면적 계산 및 누적

        # 활성 구간 업데이트
        if typ == 1:  # 시작점 이벤트
            active_intervals.append((y1, y2))  # y좌표 범위를 활성화
        else:  # 끝점 이벤트
            active_intervals.remove((y1, y2))  # y좌표 범위를 비활성화

        last_x = x  # 현재 x좌표를 이전 x좌표로 업데이트

    return total_area  # 전체 면적 반환

if __name__ == "__main__":
    li = []
    for i in range(4):
        x,y,z,e = map(int,input().split())
        li.append((x,y,z,e))
    print(solution(li))
