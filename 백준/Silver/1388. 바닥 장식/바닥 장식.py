'''

우 하 방향으로 탐색하므로 탐색 방향도 좌 상은 확인할 필요 없음

'''
import sys
input = sys.stdin.readline

di = {'-':(0,1), '|':(1,0)}

def bfs(start_x,start_y,tile): # 타일방향
    stack = [(start_x,start_y)]
    while stack:
        x,y = stack.pop(0)
        nx,ny = x + di[tile][0], y + di[tile][1]
        if 0<=nx<N and 0 <=ny < M and room[nx][ny] == tile and not visited[nx][ny]:
            visited[nx][ny] = 1
            stack.append((nx,ny))


N, M = map(int, input().split())
room = [ input().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(M):
        if visited[r][c]:
            continue
        visited[r][c] = 1
        bfs(r,c,room[r][c])
        cnt += 1

print(cnt)