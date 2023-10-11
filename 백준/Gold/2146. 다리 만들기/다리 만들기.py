'''
다리 만들기

- 섬 : 1 로 이루어진 육지
- 0 : 바다

- 두 대륙을 연결하는 가장 짧은 다리 하나

각 섬에서 BFS 탐색하다가 0이 아닌 다른 섬에서 탐색한 곳을 발견하면 그게 최소 다리길이
'''
from collections import deque

def bfs_find_island(r,c,k):
    global edge

    q = deque()
    q.append((r, c))
    arr[r][c] = k
    visited[r][c] = 0
    while q:
        i, j = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + dr, j + dc
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == -1:
                if arr[ni][nj] == 1:
                    # 연결된 섬이면
                    arr[ni][nj] = k
                    visited[ni][nj] = 0
                    q.append((ni, nj))
                # 가장자리를 큐에 넣어주자
                if arr[ni][nj] == 0:
                    arr[ni][nj] = k
                    visited[ni][nj] = 1
                    edge.append((ni,nj,k))

def bfs_bridge(edge):
    global min_dis
    # 다른 섬의 탐색 지점 만날때까지 탐색
    while edge:
        # 현재 탐색 위치
        x,y,now = edge.popleft()

        # 4방향 탐색
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            # 범위 조건 만족하고
            if 0 <= nx < N and 0 <= ny < N:
                # 만약 같은 섬이면 넘어가
                if now == arr[nx][ny]:
                    continue
                # 섬이나 다른 섬에서 이미 탐색한데면 지금까지의 최단경로랑 비교
                if visited[nx][ny]>=0 and arr[nx][ny] != now:
                    min_dis = min(visited[nx][ny] + visited[x][y],min_dis)
                # 방문하지 않은 곳이면 어느 섬에서 왔는지 정보 저장하고 큐에 추가
                if visited[nx][ny] == -1:
                    arr[nx][ny] = now
                    visited[nx][ny] = visited[x][y] + 1
                    edge.append((nx,ny,now))



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
# 가장자리 큐
edge = deque()
# 섬 구분 지어 주기
k = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] != -1 or not arr[r][c]:
            continue
        bfs_find_island(r, c, k)
        # 섬을 다 탐색했으면
        k += 1
# print(visited)
# print(edge)
min_dis = int(1e9)
# 가장자리 큐 bfs 돌리며 다른 다른 섬들의 bfs 탐색 지역 가장 먼저 만나면 거기가 최소 길이
bfs_bridge(edge)


print(min_dis)