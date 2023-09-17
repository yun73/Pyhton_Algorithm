# 2xn 타일링
# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수
dp = [0]*1001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
dp[5] = 8

n = int(input())
for i in range(5,n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n]%10007)