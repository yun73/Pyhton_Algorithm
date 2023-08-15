# 피보나치 수열
def fibo(n):
    global cnt
    cnt += 1
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

cnt = 0
print(fibo(30), cnt)


# 메모이제이션
def fibo1(n):
    global cnt1
    global memo
    cnt1 += 1
    if n < 2:
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = fibo1(n-1) + fibo1(n-2)
        return memo[n]
cnt1 = 0
N =30
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1
print(fibo1(N), cnt1)


# 피보나치 수 DP 적용 알고리즘
def fibo2(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

dp = [0] * (100 + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, 100 + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(fibo2(30))


