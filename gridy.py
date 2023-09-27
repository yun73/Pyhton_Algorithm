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

dr = [1,-1,0,0]
dc = [0,0,1,-1]
n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[1]*n for _ in range(n)]
# 이동칸 수 최대 값
max_move = 0
for r in range(n):
    for c in range(n):
        # 만약 미리 조사된 값이 있으면 넘어가
        if dp[r][c] > 1:
            continue
        # 현재 위치에서 최대 탐색 깊이 dp[r][c]
        # 4방향 탐색 후 만약 자기 보다 큰 얘 중에 dp 값이 없는 쪽으로만 
        stack = [(r,c)]
        while stack:
            # 시작 위치
            i,j = stack.pop()
            # 현재 위치에서 상하좌우 탐색
            for k in range(4):
                    ni,nj = i+dr[k], j+dc[k]
                    # 만약 나보다 작은 곳이면 
                    # dfs 탐색하면서 지나는 점들도 최대 거리가 알아서 구해짐
                    if 0<=ni<n and 0<=nj<n and forest[ni][nj] < forest[i][j]:
                        # 기존에 존재하는 거와 갱신되는 거 중에 큰 거 고르기
                        # 기존게 크다면 그 칸은 더 탐색 안해도 되고
                        if dp[ni][nj] >= dp[i][j]+1:
                             continue
                        # 아니라면 더 탐색
                        if dp[ni][nj] < dp[i][j]+1:
                            dp[ni][nj] = dp[i][j] + 1
                            stack.append((ni,nj))
                      
        print(dp)
print(max_move)

     