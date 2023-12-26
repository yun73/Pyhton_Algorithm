import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    R,G,B = map(int,input().split())
    cost.append([R,G,B])

INF = int(1e9)
ans = INF
for color in [0,1,2]: # 첫번 째 숫자를 R,G,B 중 하나로 고정

    dp = [INF,INF,INF]
    dp[color] = cost[0][color]

    for i in range(1,N):
        ndp = [0, 0, 0]
        ndp[0] = min(dp[1],dp[2]) + cost[i][0]
        ndp[1] = min(dp[0],dp[2]) + cost[i][1]
        ndp[2] = min(dp[0],dp[1]) + cost[i][2]

        dp = ndp

    ans = min(ans,min(dp[(color+1)%3],dp[(color+2)%3]))

print(ans)