# 다리 놓기
# M 개의 다리 중에 N 개의 다리 선택하기
# MCN
# nCr = n! / (n-r)!(r)!
# nCr = n-1Cr-1 + n-1Cr
# r * nCr = n * n-1Cr-1
dp = [[0]*30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            dp[i][j] = j
        else:
            if i == j:
                dp[i][j] = 1
            elif i < j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    print(dp[N][M])

