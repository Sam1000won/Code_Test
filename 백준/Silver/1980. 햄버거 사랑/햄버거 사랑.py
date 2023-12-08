'''
문제 풀이

두 햄버거를 먹는 시간 n, m 중에서 큰 값을 가장 최소로하면서 작은 값을 최대로 하면 버거의 수가 제일 많은 값
하나의 햄버거를 먹는 동안은 다른 햄버거를 먹을 수 없기 때문도 생각을 해야한다.
그리고 버거를 먹고난 다음에 남은 시간을 파악하여 더 한다.


'''
# n, m, t를 입력받는다.
n, m, t = map(int, input().split())

# n과 m 중 더 큰 값을 mx에 저장한다.
mx = max(n, m)

# n과 m 중 더 작은 값을 mn에 저장한다.
mn = min(n, m)

# burger와 coke를 초기화한다.
count = 0
burger = 0
coke = 10000

# t가 mx * count보다 크거나 같을 때까지 반복한다.
while t >= mx * count:

    # temp에 t에서 mx * count를 뺀 값을 저장한다.
    temp = t - mx * count

    # temp_burger에 count를 저장한다.
    temp_burger = count

    # temp_coke에 temp에서 mn을 나눈 몫을 저장한다.
    temp_coke = temp // mn

    # temp_burger에 temp에서 mn을 나눈 나머지를 더한다.
    temp_burger += temp % mn

    # coke가 temp_coke보다 크면, burger와 coke를 temp_burger와 temp_coke로 바꾼다.
    if coke > temp_coke:
        burger = temp_burger
        coke = temp_coke

    # coke가 temp_coke와 같고, burger가 temp_burger보다 작으면, burger와 coke를 temp_burger와 temp_coke로 바꾼다.
    elif coke == temp_coke and burger < temp_burger:
        burger = temp_burger
        coke = temp_coke

    # count를 1 증가시킨다.
    count += 1

# burger와 coke를 출력한다.
print(burger, coke)
