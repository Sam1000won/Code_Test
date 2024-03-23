import collections
import sys

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''
for k, v in list(check_word.items()):
    if v % 2 == 1: #홀수라면
        cnt += 1
        mid = k #중간에 들어갈 값으로 저장
        if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #정렬을 통해 사전순으로 for문을 돌게함
    result += (k * (v // 2)) #정확히 절반으로 나뉜 문자열을 만들어야 하므로 현재 갯수를 2로 나눠줌
print(result + mid + result[::-1]) # 앞+중간+뒤 를 더해 문자열 출력