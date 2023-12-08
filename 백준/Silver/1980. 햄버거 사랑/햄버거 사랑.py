n, m, t = map(int,input().split())

mx = max(n,m)
mn = min(n,m)

count = 0
burger = 0
coke = 10000

while t >= mx*count :
    temp = t - mx*count
    tmep_burger = count
    tmep_coke = 0
    
    tmep_burger += temp//mn
    tmep_coke += temp%mn
    
    if coke > tmep_coke:
        burger = tmep_burger
        coke = tmep_coke
    elif coke == tmep_coke and burger < tmep_burger:
        burger = tmep_burger
        coke = tmep_coke
    count += 1
    
print(f"{burger} {coke}")