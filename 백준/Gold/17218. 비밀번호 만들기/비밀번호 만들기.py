def longest_common_subsequence(a, b):
    len_a = len(a)
    len_b = len(b)
    dp = [[""] * (len_b + 1) for _ in range(len_a + 1)]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

    return dp[len_a][len_b]

a = input()
b = input()

print(longest_common_subsequence(a, b))
