# 돌게임
# 돌을 1개나 3개 가져갈 수 있음
# 2개 만들면 이기네
dp = [0] * 1001
dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "CY"
dp[5] = "Sk"

N = int(input())
for i in range(4,N+1):
    if dp[i-1] == "CY" or dp[i-3] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"

print(dp[N])