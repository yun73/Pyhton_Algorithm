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
                if arr[ni][nj] == 1: # 연결된 섬이면 탐색
                    arr[ni][nj] = k
                    visited[ni][nj] = 0
                    q.append((ni, nj))
                if arr[ni][nj] == 0: # 가장자리면 edge 배열에 넣기
                    arr[ni][nj] = k
                    visited[ni][nj] = 1
                    edge.append((ni,nj,k))

def bfs_bridge(edge):
    global min_dis
    # 다른 섬의 탐색 지점 만날때까지 탐색
    while edge:
        # 각 차례의 edge 들을 다 돌았을 때 최소 값이 나왔다면 종료
        if min_dis != int(1e9):
            return
        
        for _ in range(len(edge)): # 현재 배열에 담긴 가장 자리들 수만큼만 반복
            # 현재 탐색 위치
            x,y,now = edge.popleft()
    
            # 4방향 탐색
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # 범위 조건 만족하고
                if 0 <= nx < N and 0 <= ny < N:
                    # 만약 같은 섬이면 건너뛰기
                    if now == arr[nx][ny]:
                        continue
                    # 섬이나 다른 섬에서 이미 탐색한 곳이면 최단경로랑 비교
                    if visited[nx][ny] >= 0 and arr[nx][ny] != now:
                        min_dis = min(visited[nx][ny] + visited[x][y],min_dis)
                    # 방문하지 않은 곳이면 어느 섬에서 왔는지 정보 저장하고 큐에 추가
                    if visited[nx][ny] == -1:
                        arr[nx][ny] = now
                        visited[nx][ny] = visited[x][y] + 1
                        edge.append((nx,ny,now))



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
# 섬 가장자리 큐
edge = deque()
k = 1 # 섬 번호
for r in range(N):
    for c in range(N):
        if visited[r][c] != -1 or not arr[r][c]:
            continue
        bfs_find_island(r, c, k) # k 번을 들고 섬 탐색
        k += 1

min_dis = int(1e9)
# 가장자리 큐 bfs 돌리다 다른 섬에서 시작한 탐색 지역 만나면 해당 지역이 최단 거리
bfs_bridge(edge)

print(min_dis)