def re(N):
    global cnt
    cnt += 1
    if dp[N] == 0:
        for i in range(1,5):
            if i == 2:
                continue
            if re(N-i) == -1:
                dp[N] = 1
                break
        else:
            dp[N] = -1

    return dp[N]

cnt = 0
N = int(input())
dp = [0] * 1001

dp[1] = 1  # 'SK'
dp[2] = -1  # 'CY'
dp[3] = 1
dp[4] = 1
dp[5] = 1
dp[6] = 1
dp[7] = -1
dp[8] = 1
dp[9] = -1

re(N)
if dp[N] == 1:
    print('SK')
else:
    print('CY')

print(cnt)