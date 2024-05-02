N = int(input())

for _ in range(N):
    a = int(input())
    lst_a = set(map(int, input().split()))
    b = int(input())
    lst_b = set(map(int, input().split()))
    c = int(input())
    lst_c = set(map(int, input().split()))
    res = set()  # 결과를 중복없이 저장하기 위해 set으로 선언

    for i in lst_a:
        for j in lst_b:
            for k in lst_c:
                total = i + j + k
                if all(char in {'5', '8'} for char in str(total)):
                    res.add(total)  # 중복된 결과가 제거됨

    print(len(res))
