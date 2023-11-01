# [Silver IV] 듣보잡 - 1764 

[문제 링크](https://www.acmicpc.net/problem/1764) 

### 성능 요약

메모리: 43924 KB, 시간: 3904 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 정렬, 문자열

### 제출 일자

2023년 11월 1일 09:23:36

### 문제 설명

<p>김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.</p>

<p>듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.</p>

### 출력 

 <p>듣보잡의 수와 그 명단을 사전순으로 출력한다.</p>

### 문제 풀이

'''
처음 입력값을 명단이니까 값을 하나하나로 받아서 리스트에 담음

n, m = map(int, input().split())
all_li = n + m
name_li = []
for i in range(all_li):
    name = input()
    name_li.append(name)

duplicates = [name for name in name_li if name_li.count(name) > 1]
duplicates = list(set(duplicates)) 

print(len(duplicates))
for name in duplicates:
    print(name)
'''    
결과는 시간초과 및 틀림. 

문제를 다시보니까 입력값을 2개 즉 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때
이런식으로 나옴
그래서 각 입력값을 받고 중복값을 찾음
'''
n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())

res = sorted(list(a & b))

print(len(res))
for i in res:
    print(i)
'''
