# 퇴사
N = int(input())
con = [[0] * N for _ in range(2)]
for i in range(N):
    T, P = map(int, input().split())
    con[0][i] = T
    con[1][i] = P

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    # 마지막에서부터 해당 칸 까지의 최대 값
    if i + con[0][i] > N :
        dp[i] = max(dp[i:N])
    else:
        # 현재 까지 내 뒤에 올 수 있는 최대값 구해가
        # 갱신할 값이 해당일수 내에 있는 최대값보다 크면 갱신
        if dp[i + con[0][i]] + con[1][i] > max(dp[i+1:i + con[0][i]+1]):
            dp[i] = dp[i + con[0][i]] + con[1][i]
        else: # 아니면 최고값 가져오기
            dp[i] = max(dp[i+1:i + con[0][i]+1])

print(dp[0])