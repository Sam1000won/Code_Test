n = int(input())

length = len(str(n))
result = 0
for i in range(length):
    digit = n%10
    n = n//10

    if digit >4:
        result += (digit-1) * (9**i)
    else:
        result += digit * (9**i)
print(result)
