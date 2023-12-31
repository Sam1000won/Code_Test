# 입력 받는 tjfxkd 질량
sugar = int(input())

# 가방안에 담을 설탕
bag = 0

# 조건문 설정
while sugar >= 0:
	if sugar % 5 == 0:
		bag += (sugar // 5) # 5로 나눈 몫을 구함
		print(bag) # 5로 나누어 떨어지면 가방에 바로 넣음
		break # 조권문 탈출
	sugar -= 3
	bag += 1 # 5의 배수가 될때까지 -3, 봉지 +1
else:
	print(-1)