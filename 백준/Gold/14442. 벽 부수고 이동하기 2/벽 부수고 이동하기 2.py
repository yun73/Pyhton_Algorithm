'''
벽 부수고 이동하기2

- 맵 : N x M 크기
    - 0 : 이동 가능
    - 1 : 벽

- 이동 : 1,1 > N,M 까지
    - 최단 경로로
    - k 번 만큼 벽을 뚫을 수 있음

- 최단 거리로 도착점 까지 가야 하므로 bfs 로 하자
- 현재 벽을 부순 개수를 기록하며 탐색
    - visited 처리를 벽을 부순 개수에 따라 처리해주자
    - 만약 k 번 부순 자리에 먼저 도착한 경우가 있다면
    - BFS 이므로 먼저 들어온 얘가 무조건 최단 거리임
'''
import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
arr = [input().rstrip() for _ in range(N)]
# print(arr)
# k = 0, 즉 하나도 안부순 경우도 있으므로 K+1 개만큼 생성
visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
# print(visited)
def bfs(start):
    q = deque()
    q.append((start,start,0))
    visited[0][0][0] = 1
    while q:
        x,y,cnt = q.popleft()
        # 만약 도착점에 도달하면 최단 거리 출력
        if (x,y) == (N-1,M-1):
            return visited[cnt][x][y]
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and cnt <= K:
                # 만약 벽이고 부순 횟수가 K 보다 작으면,그리고 K+1 부순 위치에 아직 방문하지 않았다면
                if arr[nx][ny] == '1' and cnt < K and not visited[cnt+1][nx][ny]:
                    visited[cnt+1][nx][ny] = visited[cnt][x][y] + 1
                    q.append((nx,ny,cnt+1))
                    continue
                # 만약 벽이 아니라면
                elif arr[nx][ny] == '0':
                    if visited[cnt][nx][ny]:
                        continue
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    q.append((nx,ny,cnt))
    # 못 도착하면 -1 반환
    else:
        return -1

print(bfs(0))


