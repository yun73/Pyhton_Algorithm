'''
로봇 청소기

- 직사각형 방 : w x h
    - . : 깨끗한 칸
    - * : 더러운 칸
    - x : 가구
    - o : 로봇 청소기의 시작 위치

- 로봇청소기
    - 가구로 이동 불가
    - 더러운 칸 방문해서 깨끗하게


'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr,sc,find):
    q = deque()
    q.append((sr,sc,find))
    visited[find][sr][sc] = 1

    while q:
        x,y,find = q.popleft()
        if find == (1<<d) -1:
            return visited[find][x][y] - 1

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx, y+dy
            if 0<=nx<h and 0<=ny<w and not visited[find][nx][ny]:
                visited[find][nx][ny] = visited[find][x][y] + 1
                if room[nx][ny] == 'x':
                    continue
                if str(room[nx][ny]) in '.o':
                    q.append((nx,ny,find))
                    continue
                # 쓰레기 만났는데
                # 이미 해당 영역에 포함되어 있는 더러운 공간이면 패스
                if find & (1 << room[nx][ny]):
                    q.append((nx, ny, find))
                    continue
                next = find + (1 << room[nx][ny])
                visited[next][nx][ny] = visited[find][x][y] + 1
                q.append((nx, ny, next))
    else:
        return -1

while True:
    w, h = map(int, input().split())
    if (w,h) == (0,0):
        break
    sr,sc = 0,0
    dirty = 0
    d = 0
    room = [list(input()) for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if room[r][c] in '.x':
                continue
            if room[r][c] == 'o':
                sr,sc = r,c
                continue
            room[r][c] = d
            d += 1

    visited = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(1<<d)]

    print(bfs(sr,sc,0))

