def f(n):
    # n개의 항목에서 선택할 수 있는 경우의 수를 나타내는 함수
    # 이 함수는 주어진 n에 대해 그룹의 시작 번호를 계산합니다.
    return 1 + n * (n - 1) // 2

def cdp(max_n):
    # 최대 n에 대해 DP 테이블을 생성하는 함수
    # dp[i]는 그룹 i의 시작 번호를 저장합니다.
    dp = [0] * (max_n + 1)  # DP 배열 초기화
    for i in range(max_n + 1):
        dp[i] = f(i)  # 각 그룹의 시작 번호를 f(i)로 계산하여 저장
    return dp

def solution(x, dp):
    # 주어진 x가 속하는 그룹과 해당 그룹의 시작 번호를 찾는 함수
    n = 1  # 그룹 번호 초기화
    while True:
        if x == 1:
            return 1, 1  # x가 1일 경우 그룹 1과 시작 번호 1 반환
        if dp[n] <= x < dp[n + 1]:
            return n, dp[n]  # x가 dp[n]과 dp[n+1] 사이에 있을 경우 그룹 n과 시작 번호 반환
        n += 1  # 다음 그룹으로 이동

# 사용자로부터 입력을 받는 부분
n = int(input())  # 쿼리의 수를 입력받음
q = [tuple(map(int, input().split())) for _ in range(n)]  # 쿼리 쌍 입력받기

# 입력된 쿼리에서 최대 N1과 N2를 찾음
max_value = max(max(N1, N2) for N1, N2 in q)  
dp = cdp(max_value)  # DP 테이블 생성

# 각 쿼리에 대해 그룹과 좌표를 계산
for N1, N2 in q:
    # N1에 대한 그룹과 시작 번호 계산
    group1, start_num_1 = solution(N1, dp)
    # N2에 대한 그룹과 시작 번호 계산
    group2, start_num_2 = solution(N2, dp)

    sum1, sum2 = group1 + 1, group2 + 1  # 각 그룹의 크기를 계산

    # N1의 좌표 계산
    N1_X = 1 + N1 - start_num_1  # X좌표
    N1_Y = sum1 - 1 - N1 + start_num_1  # Y좌표

    # N2의 좌표 계산
    N2_X = 1 + N2 - start_num_2  # X좌표
    N2_Y = sum2 - 1 - N2 + start_num_2  # Y좌표

    # 최종 좌표 계산
    X, Y = N1_X + N2_X, N1_Y + N2_Y
    GROUP = X + Y  # 최종 그룹 값 계산

    # 결과 출력: GROUP - 1에 대한 f의 값을 계산하고, X - 1을 더해 출력
    print(f(GROUP - 1) + (X - 1))
