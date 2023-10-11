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
    visited[r][c] = k
    while q:
        i, j = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + dr, j + dc
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == 1:
                    # 연결된 섬이면
                    arr[ni][nj] = k
                    visited[ni][nj] = k
                    q.append((ni, nj))
                # 가장자리를 큐에 넣어주자
                if arr[ni][nj] == 0:
                    visited[ni][nj] = k
                    edge.append((ni,nj,k))




N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
# 가장자리 큐
edge = deque()
# 섬 구분 지어 주기
k = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] or not arr[r][c]:
            continue
        bfs_find_island(r, c, k)
        # 섬을 다 탐색했으면
        k += 1

min_dist = int(1e9)
# 가장자리 큐 bfs 돌리며 다른 다른 섬들의 bfs 탐색 지역 가장 먼저 만나면 거기가 최소 길이



print(min_dist-1)