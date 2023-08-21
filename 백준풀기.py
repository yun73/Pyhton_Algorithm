# 퇴사
N = int(input())
con = [[0]*N for _ in range(2)]
for i in range(N):
    T, P = map(int, input().split())
    con[0][i] = T
    con[1][i] = P

dp = [0] * (N+1)

for i in range(N-1,-1,-1):
    # 마지막에서부터 해당 칸 까지의 최대 값
    if i + con[0][i] -1  > N-1:
        dp[i] = 0
    else:
        # 현재 까지 내 뒤에 올 수 있는 최대값 구해가
        max_now = max(dp[i + con[0][i]:])
        if dp[i+con[0][i]] > max_now:
            dp[i] = dp[i+con[0][i]] + con[1][i]
        else:
            dp[i] = max_now + con[1][i]

print(dp[0])
