a = input()
b = input()

len_a = len(a)
len_b = len(b)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(1, len_a + 1):
    for j in range(1, len_b + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

res = ''
i = len_a
j = len_b

while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        res = a[i - 1] + res
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(res)
