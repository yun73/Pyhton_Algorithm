'''
부산의 해적

- 보물지도 : NxM
    - 수아 : Y
    - 해적 : V
    - 섬 : I
    - 바다 : .

- 이동 상하좌우
- 해적
    - 매번 수아가 이동한 후, 해적은 수아의 이동에 대해서 이동할지 멈춰있을지 결정

- 해적과 수직선, 수평선상에 수아가 있고, 오직 그 사이에 바다만 있을 때 수아는 죽는다.
- 만약, 수아가 아직 죽지 않았고, 보물 위치에 있다면, 수아는 보물은 얻은 것이다.

- 해적을 먼저 움직여서 각 칸들이 해적이 몇번움직였을 때 위험한 지 저장하자
- 각 칸에는 최소로 움직였을 때 죽일수 있는 경우가 우선적으로 와야 함
- 그러면서 동시에 움직이면서 갱신도 해줘야 해
'''
import sys
from collections import deque
input = sys.stdin.readline

# 해적 움직임
def V_move(q):
    while q:
        x, y = q.popleft()
        # 현재 위치에서 죽일 수 있는 곳 다 표시하고 상하좌우 이동
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):

            nx,ny = x+dx,y+dy
            # 일단 범위 벗어나면 브레이크
            if not(0<=nx<N and 0<=ny<M):
                continue
            # 섬 나오면 break
            if arr[nx][ny] == 'I':
                continue

            if visited[nx][ny] == INF:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    # 다 끝나면 arr 에 최소 값들만 저장
    for i in range(N):
        stack = []
        val = [0, 0, float('inf')]  # 좌표 idx_0 ~ idx_1 까지 idx_2값으로 채움
        for j in range(M):
            if arr[i][j] != 'I':
                val[2] = min(val[2], visited[i][j]); val[1] = j
            elif arr[i][j] == 'I' and val[2] != float('inf'):
                stack.append(val)
                val = [j + 1, j + 1, float('inf')]
            else:
                val = [j + 1, j + 1, float('inf')]
        if val[2] != float('inf'): stack.append(val)
        for s, e, val in stack:
            for j in range(s, e + 1):
                arr[i][j] = val

    for j in range(M):
        stack = []
        val = [0, 0, float('inf')]  # 좌표 idx_0 ~ idx_1 까지 idx_2값으로 채움
        for i in range(N):
            if arr[i][j] != 'I':
                val[2] = min(val[2], visited[i][j]); val[1] = i
            elif arr[i][j] == 'I' and val[2] != float('inf'):
                stack.append(val)
                val = [i + 1, i + 1, float('inf')]
            else:
                val = [i + 1, i + 1, float('inf')]
        if val[2] != float('inf'): stack.append(val)
        for s, e, val in stack:
            for i in range(s, e + 1):
                arr[i][j] = min(arr[i][j], val)

def find_treasure(sr,sc):
    go = deque()
    go.append((sr,sc))
    visit[sr][sc] = 0
    while go:
        x,y = go.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'I' and visit[nx][ny] == -1 and visit[x][y] + 1 < arr[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1
                go.append((nx,ny))

    if visit[tr][tc] != -1 and visit[tr][tc] < visited[tr][tc]:
        return 'YES'
    else:
        return 'NO'


N,M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
# print(arr)
INF = int(1e9)
visited = [[INF]*M for _ in range(N)]
visit = [[-1]*M for _ in range(N)]
sr,sc = 0,0
tr,tc = 0,0
q = deque()
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'I':
            continue
        if arr[r][c] == '.':
            arr[r][c] = INF
            continue
        if arr[r][c] == 'Y':
            sr,sc = r,c
            arr[r][c] = INF
            continue
        if arr[r][c] == 'T':
            tr, tc = r, c
            arr[r][c] = INF
            continue
        if arr[r][c] == 'V':
            q.append((r,c))
            arr[r][c] = 0
            visited[r][c] = 0
            continue

V_move(q)
# print(min(visited[1]))
print(find_treasure(sr,sc))
# for line in visited:
#     print(*line)
# print('-----')
# for line in arr:
#     print(*line)
# print('-----')
# for line in visit:
#     print(*line)


