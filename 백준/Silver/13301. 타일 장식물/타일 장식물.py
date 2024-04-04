import sys

imput = sys.stdin.readline

num = int(input())

dp = [0]*(num +2)
dp[1] = 1

for i in range(2, num+2):
	dp[i] = dp[i-1] +dp[i-2]

print((dp[num]+dp[num+1])*2)
