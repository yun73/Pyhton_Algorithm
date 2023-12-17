import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

di = [(0,1),(1,0)] # 우, 하
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if (x,y) == (N-1,N-1):
            print(dp[x][y])
            break
        nx = x + board[x][y]
        ny = y + board[x][y]
        # 만약 현재 위치에서 우, 하 방향으로 갈 수 있는 위치가 범위 안에 있다면
        if  nx < N:
            dp[nx][y] = dp[nx][y] + dp[x][y]

        if ny < N:
            dp[x][ny] = dp[x][ny] + dp[x][y]

