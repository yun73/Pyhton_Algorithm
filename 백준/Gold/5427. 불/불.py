'''
'.': 빈 공간
'#': 벽
'@': 상근이의 시작 위치
'*': 불
근이가 있는 칸에
불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다
'''
import sys
from collections import deque
input = sys.stdin.readline

# 불 번짐
def fire_spreads(fire):
    while fire:
        x,y = fire.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<h and 0<=ny<w and building[nx][ny] == '.':
                building[nx][ny] = building[x][y] + 1
                fire.append((nx,ny))

def escape(sr,sc):
    visited = [[0]*w for _ in range(h)]
    q = deque([(sr,sc)])
    visited[sr][sc] = 1
    while q:
        x,y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] == '#' or visited[nx][ny] != 0:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                if building[nx][ny] == '.': # 불이 아이에 안닿는곳
                    q.append((nx,ny))
                else: # 불이 닿는 곳
                    if building[nx][ny] <= visited[x][y]:
                        continue
                    q.append((nx, ny))
            else:
                return visited[x][y]
    else:
        return 'IMPOSSIBLE'

T = int(input())
for tc in range(T):
    w,h = map(int, input().split())
    building = [list(input().rstrip()) for _ in range(h)]
    sr,sc = -1,-1
    fire = deque([])
    for r in range(h):
        for c in range(w):
            if building[r][c] in '.#':
                continue
            elif building[r][c] == '*':
                fire.append((r,c))
                building[r][c] = 0
            elif building[r][c] == '@':
                sr,sc = r,c
                building[r][c] = '.'

    if fire:
        fire_spreads(fire)
    print(escape(sr,sc))


