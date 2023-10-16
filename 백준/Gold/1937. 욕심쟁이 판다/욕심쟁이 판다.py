'''
욕심쟁이 판다

- 대나무 숲 : nxn 크기

- 대나무 다 먹으면 => 상하좌우 중 한 곳으로 이동

- 조건
    - 욕심이 매우 많아 대나무 먹고 자리 옮기면 옮긴 지역의 대나무 전 지역보다 많아야 함

- 판다가 최대한 많은 칸 이동하려면 어떤 경로로 가야해?
- 이동할 수 있는 칸의 최대값

이동한 칸 기준 전에 있던 칸은 항상 대나무가 적을 거야
그러면 처음에 각 위치마다 대나무 큰 지역이 몇 개 있는지 기록
근데 몇개 있는지 기록하는 것만으로는 부족할 거 같은데

- 현재지역보다 큰 곳 가야함
- 해당 위치 까지 오는데의 거리가 계속 갱신됨


최악의 경우 500*500*4방향*깊이?
'''
import sys
limit_number = int(1e6)
sys.setrecursionlimit(limit_number)

di = [[1,0],[-1,0],[0,1],[0,-1]]
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
# dp[x][y] 는 해당 위치에서 갈 수 있는 최장 거리를 기록
dp = [[0]*n for _ in range(n)]
max_move = 0
def dfs(x,y):
    # 만약 이미 값이 존재하지 않을 때만 진행
    if not dp[x][y]:
        # 기본값
        dp[x][y] = 1
        # 4방향 탐색
        for dx, dy in di:
            nx,ny = x+dx, y+dy
            # 만약 탐색방향이 범위안에 있고, 현재 위치보다 큰 곳이면
            if 0<=nx<n and 0<= ny <n and forest[nx][ny] > forest[x][y]:
                # 탐색하는 모든 칸의 dp 값이 저장 됨
                # 이때 항상 최장거리를 위에서 부터 저장해오므로
                dp[x][y] = max(dp[x][y], dfs(nx,ny))

    # 재귀 돌게 되는 각 위치의 dp 값도 만들어진다.
    # 만약 하나도 갈 수 있는데 없으면
    return dp[x][y] + 1

for r in range(n):
    for c in range(n):
        # 각 위치에 대해서 dfs 값을 dp에 저장하며
        # 최장거리 갱신
        if dp[r][c]:
            max_move = max(max_move,dp[r][c])
            continue
        max_move = max(max_move, dfs(r, c))

print(max_move-1)