a = input()
b = input()

len_a = len(a)
len_b = len(b)

dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]

for i in range(len_a):
    for j in range(len_b):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

res = ''
while dp[len_a][len_b] != 0:
    if dp[len_a][len_b] == dp[len_a - 1][len_b]:
        len_a -= 1
    elif dp[len_a][len_b] == dp[len_a][len_b - 1]:
        len_b -= 1
    else:
        res += a[len_a - 1]
        len_a -= 1
        len_b -= 1

print(res[::-1])
