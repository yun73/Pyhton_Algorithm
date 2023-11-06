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
        x, y, turn = q.popleft()
        # 현재 위치에서 죽일 수 있는 곳 다 표시하고 상하좌우 이동
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            for dis in range(1,max(N,M)-1):
                nx,ny = x+dis*dx,y+dis*dy
                # 범위 넘어가면 해당 방향으로 더 못감
                if not(0<=nx<N and 0<=ny<M):
                    break
                # 섬 만나면 못감
                if arr[nx][ny] == 'I':
                    break
                if dis == 1:
                    q.append((nx, ny, turn + 1))
                if visited[nx][ny] != INF:
                    break


                # 내가 지금 보는 턴 보다 큰 곳 기록
                if turn < visited[nx][ny]:
                    visited[nx][ny] = turn
                



N,M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
# print(arr)
INF = int(1e9)
visited = [[0]*M for _ in range(N)]
sr,sc = 0,0
q = deque()
i = 0
for r in range(N):
    for c in range(M):
        if i == 2:
            break
        if arr[r][c] in '.I':
            arr[r][c] = INF
            continue
        if arr[r][c] == 'Y':
            sr,sc = r,c
            arr[r][c] = INF
            i +=1
            continue
        if arr[r][c] == 'V':
            q.append((r,c,1))
            arr[r][c] = 1
            visited[r][c] = 1
            i +=1
            continue

V_move(q)

for line in visited:
    print(*line)

