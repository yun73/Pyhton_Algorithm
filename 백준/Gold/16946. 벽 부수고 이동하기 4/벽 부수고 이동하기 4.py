'''
벽 부수고 이동하기2

- 맵 : N x M 크기
    - 0 : 이동 가능
    - 1 : 벽

- 이동 : 상하좌우
- 해당 벽 부쉈을 때 이동할 수 있는 칸의 개수를 기록
- 새로운 배열을 만들어주고
    - 벽이 아닌 구간에서 BFS 를 돌려주고
    - 다 돌면 돌 수 있는 개수를 지나다니면서 만난 벽들에 개수를 추가해줘

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr,sc):
    q = deque()
    wall = set()
    cnt = 1
    q.append((sr,sc))
    visited[sr][sc] = 1
    res[sr][sc] = 0
    while q:
        x,y = q.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == '0' and not visited[nx][ny]:
                    res[nx][ny] = 0
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt += 1
                    continue
                if arr[nx][ny] == '1':
                    wall.add((nx,ny))

    for i,j in wall:
        res[i][j] += cnt


N,M = map(int,input().split())
arr = [input().rstrip() for _ in range(N)]
res = [[1]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# print(visited)
for r in range(N):
    for c in range(M):
        if visited[r][c] or arr[r][c] == '1':
            continue
        if arr[r][c] == '0' and not visited[r][c]:
            bfs(r,c)

for r in range(N):
    for c in range(M):
        print(res[r][c]%10, end = '')
    print()


