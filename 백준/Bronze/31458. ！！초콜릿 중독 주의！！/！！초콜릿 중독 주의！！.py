t = int(input())
for _ in range(t):
    operation = input().rstrip()
    flag = True
    l_cnt = 0
    res = 0

    for i in operation:
        if i == '!' and flag:
            l_cnt += 1
        elif i != '!':
            flag = False
            res = int(i)
        elif i == '!' and flag == False:
            res = 1

    if res == 0:
        if l_cnt % 2 == 0:
            res = 0
        else:
            res = 1
    else:
        if l_cnt % 2 == 0:
            res = 1
        else:
            res = 0

    print(res)