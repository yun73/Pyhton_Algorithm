'''
동전 1,2,5,7 - 4종류
동전 개수 최소가 되도록 지불

남은 금액이 i 일 때의 최소 동전 개수

'''
N = int(input())

dp = [i for i in range(N+1)]

for i in range(2,N+1):
    dp[i] = dp[i-1] + 1
    if i >= 2:
        dp[i] = min(dp[i],dp[i-2] + 1)
    if i >= 5:
        dp[i] = min(dp[i],dp[i-5] + 1)
    if i >= 7:
        dp[i] = min(dp[i],dp[i-7] + 1)

print(dp[N])