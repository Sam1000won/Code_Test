# 아부지의 색
fBody, fTail = map(str, input().split())

# 어무니의 색
mBody, mTail = map(str, input().split())

# answer 값
color = []

# 아무지의 색이 컬러에 없다면 아무지의 몸색 추가
if fBody not in color:
	color.append(fBody)

# 아무지의 색이 컬러에 없다면 아무지의 꼬리색 추가
if fTail not in color:
	color.append(fTail)

# 어무니의 색이 컬러에 없다면 어무니의 몸색 추가
if mBody not in color:
	color.append(mBody)

# 아무지의 색이 컬러에 없다면 어무지의 꼬리색 추가
if mTail not in color:
	color.append(mTail)
# 사전순으로 컬러색 정렬
color.sort()

# 컬러를 순차적으로 출력
for i in range(0,len(color)):
	for j in range(0,len(color)):
		print(color[i], color[j])