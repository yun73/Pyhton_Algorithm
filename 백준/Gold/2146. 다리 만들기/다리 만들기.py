'''
다리 만들기

- 섬 : 1 로 이루어진 육지
- 0 : 바다

- 두 대륙을 연결하는 가장 짧은 다리 하나

각 섬에서 BFS 탐색하다가 0이 아닌 다른 섬에서 탐색한 곳을 발견하면 그게 최소다리길이
- 근데 이거는 구현이 어려움

그냥 섬에서 bfs로 다른 섬 도달하면 그게 해당 섬에서의 최소 길이이고 각 섬마다의
최소 길이들 중 가장 작은 거 얻기

1. 섬마다 구분해주는 BFS 한번 돌기
2. 각 섬에서 다른섬까지의 최소 거리 찾기

'''
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
# 섬 구분 지어 주기
k = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] or not arr[r][c]:
            continue
        q = deque()
        q.append((r, c))
        arr[r][c] = k
        visited[r][c] = True
        while q:
            i, j = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dr, j + dc
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 1 and not visited[ni][nj]:
                        # 연결된 섬이면
                        arr[ni][nj] = k
                        visited[ni][nj] = True
                        q.append((ni, nj))
        # 섬을 다 탐색했으면
        k += 1

min_dist = int(1e9)
# 각 섬에서 bfs 돌리며 다른 섬들까지의 거리의 최소 값 구하기
for i in range(1, k):
    visit = [[0] * N for _ in range(N)]
    q = deque()

    for r in range(N):
        for c in range(N):
            if arr[r][c] == i:
                visit[r][c] = 1
                q.append((r, c))

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                # 다른섬 도착
                if arr[nx][ny] > 0 and arr[nx][ny] != i:
                    min_dist = min(min_dist,visit[x][y])
                    break
                # 바다, 방문 안했던 곳이면
                if arr[nx][ny] == 0 and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))

print(min_dist-1)