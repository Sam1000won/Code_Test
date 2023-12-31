import sys

# 테스트 케이스의 수
case = int(sys.stdin.readline())

for _ in range(case):
    # 문서의 개수 N,  몇 번째로 인쇄되었는지 궁금한 문서가 
    # 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
    n, m = map(int, sys.stdin.readline().split())
    
    # N개 문서의 중요도
    priority = list(map(int, sys.stdin.readline().split()))
    
    # N개 문서의 기존 순서 저장
    index = [i for i in range(n)]
    
    # 몇 번째로 인쇄할지 카운트하는 변수
    count = 0
    
    while True:
        # 현재 문서가 중요도가 제일 높다면
        if priority[0] == max(priority):
            # 몇 번째로 출력 되는지 카운트
            count += 1
            # 궁금한 문서인지 확인
            if index[0] == m:
                print(count)
                break
            # 궁금한 문서가 아니라면 리스트에서 탈출
            else:
                del priority[0]
                del index[0]
        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면
        else:
            # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치
            priority.append(priority[0])
            del priority[0]
            index.append(index[0])
            del index[0]