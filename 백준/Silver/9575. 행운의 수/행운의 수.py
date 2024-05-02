from itertools import product

N = int(input())

for _ in range(N):
    a = int(input())
    lst_a = set(map(int, input().split()))
    b = int(input())
    lst_b = set(map(int, input().split()))
    c = int(input())
    lst_c = set(map(int, input().split()))

    res = set()
    
    for combination in product(lst_a, lst_b, lst_c):
        total = sum(combination)
        if all(char in {'5', '8'} for char in str(total)):
            res.add(total)

    print(len(res))