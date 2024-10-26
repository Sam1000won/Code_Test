import sys

# 첫 번째 입력으로 들어오는 정수 m을 읽어들여서 운영할 명령의 수를 결정합니다.
m = int(sys.stdin.readline())
# 집합 S를 초기화합니다. 이 집합은 1부터 20까지의 정수를 저장하는데 사용됩니다.
S = set()

# m만큼 반복하여 명령을 처리합니다.
for _ in range(m):
    # 한 줄의 명령을 읽어들여서 공백으로 나누고 리스트로 만듭니다.
    temp = sys.stdin.readline().strip().split()
    
    # 명령이 하나만 있을 경우 (예: "all" 또는 "empty" 처리)
    if len(temp) == 1:
        # "all" 명령이 들어오면 S를 1부터 20까지의 정수로 채웁니다.
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        # 다른 경우 (예: "empty")에는 S를 빈 집합으로 초기화합니다.
        else:
            S = set()
    
    # 명령이 두 개 있을 경우 (예: "add x", "remove x", "check x", "toggle x" 처리)
    else:
        func, x = temp[0], temp[1]  # 첫 번째 요소는 함수, 두 번째는 정수 x입니다.
        x = int(x)  # x를 정수로 변환합니다.

        # 각 명령에 따라 집합 S를 조작합니다.
        if func == "add":
            # x를 집합 S에 추가합니다.
            S.add(x)
        elif func == "remove":
            # x를 집합 S에서 제거합니다. (x가 존재하지 않아도 에러가 발생하지 않도록 discard 사용)
            S.discard(x)
        elif func == "check":
            # x가 집합 S에 존재하는지 확인하고, 결과에 따라 1 또는 0을 출력합니다.
            print(1 if x in S else 0)
        elif func == "toggle":
            # x가 집합 S에 존재하면 제거하고, 존재하지 않으면 추가합니다.
            if x in S:
                S.discard(x)
            else:
                S.add(x)
