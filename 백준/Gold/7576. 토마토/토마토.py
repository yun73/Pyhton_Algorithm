'''
토마토

- 현재 토마토 익으면 하루 뒤에 상하좌우 익게 한다

'''
import sys
from collections import deque
input = sys.stdin.readline
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(ripe):
    global visited

    new_ripe = deque()
    while ripe:
        x,y = ripe.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and box[nx][ny] == 0:
                visited[nx][ny] = 1
                new_ripe.append((nx,ny))

    return new_ripe

M,N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
# 익은 토마토가 있는칸 모두 조사
ripe = deque()
cnt = 0
for r in range(N):
    for c in range(M):
        if box[r][c] == -1:
            continue
        if box[r][c] == 1:
            ripe.append((r, c))
            visited[r][c] = 1
        cnt += 1


if not ripe:
    print(-1)
else:
    cnt -= len(ripe)
    day = 0
    while cnt>0:
        if not ripe:
            break
        ripe = bfs(ripe)
        cnt -= len(ripe)
        day += 1
    if cnt > 0:
        print(-1)
    else:
        print(day)
