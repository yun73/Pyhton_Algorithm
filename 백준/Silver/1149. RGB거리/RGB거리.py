import sys
input = sys.stdin.readline

N = int(input())

dp = list(map(int,input().split()))
for _ in range(N-1):
    cost = list(map(int,input().split()))
    new_dp = [0,0,0]
    for color in range(3):
        new_dp[color] = min(cost[color] + dp[(color+1)%3],cost[color] + dp[(color+2)%3])

    dp = new_dp

print(min(dp))