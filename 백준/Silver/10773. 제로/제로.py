# 장부 리스트 
jangbo = int(input())

# 장부 스택
number_stk = []

# 장부에 숫자 넣기
for i in range(jangbo):
	num = int(input())
	if (num == 0): # 숫자가 0이 들어가면 pop
		number_stk.pop()
	else: # 아닐 경우 추가
		number_stk.append(num)
# 스택의 합 계산
print(sum(number_stk))