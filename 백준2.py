'''
거의 최단 경로

'''


'''
거울 설치

- 집
    - 문 : '#' : 2개
    - 양면거울 : '!'
        - 45도 기울어진 대각선 방향
        - 즉 90 도 꺾는 거만 가능하다
    - 벽 : '*'
    - 빈공간 : '.'

- 설치해야할 거울의 최소 개수
- 문부터 시작하여 다른 문을 향해 탐색한다
- 각 위치에는 해당 위치까지 오는데의 최소 거울 개수를 기록해준다
- 빛은 탐색을 일직선 방향으로 밖에 못한다.
- 일직선 탐색시 거울 설치할 수 있는 곳 나오면 좌우로 최소 거울의 개수 추가
- 근데 최소 거리여도 오는 방향이 총 4군데가 가능하다
- 따라서 visited 4차원으로 만들어주자

'''

import sys, heapq
from collections import deque
input = sys.stdin.readline

# 방향
# 상하좌우
di = [(-1,0),(1,0),(0,-1),(0,1)]
op_di = {0:1,1:0,2:3,3:2}

def is_valid(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    return False

N = int(input())
house = [list(input().strip()) for _ in range(N)]

# 문 위치를 찾자
i=0
door={}
for r in range(N):
    for c in range(N):
        if house[r][c] == '#':
            door[i]=(r,c)
            i+=1
        if i ==2: break
    if i ==2: break

#
def bfs(door):
    INF = int(1e9)
    visited = [[[INF]*4 for _ in range(N)] for _ in range(N)]
    # 탐색할 우선순위 큐 생성
    # 지금 거리까지 오는 최소 거울 개수,이전 방향,x,y
    sr,sc = door[0][0], door[0][1]
    end_x, end_y = door[1][0], door[1][1]
    pq = deque([])
    for i in range(4):
        visited[sr][sc][i] = 0
        pq.append((0,i,sr,sc))

    while pq:
        mirror, before, x, y = pq.popleft()
        # if (x,y) == (end_x,end_y):
        #     return mirror
        # 지금 방향 일직선으로 쭉 탐색
        for dis in range(N):
            nx,ny = x+dis*di[before][0], y+dis*di[before][1]
            # 경계 밖이면 종료
            if not is_valid(nx,ny):
                break
            # 만약 벽이면 종료하고
            if house[nx][ny] == '*':
                break
            # 만약 빈칸이면 최소거울개수 그대로 받아서 넘어가고
            if visited[nx][ny][before] < mirror:
                continue
            visited[nx][ny][before] = mirror

            # 만약 거울이면 해당 위치에서 90도 방향으로 최소 거울 개수 1 추가해주고
            if house[nx][ny] == '!':
                for d in range(4):
                    # 이전과 같은 방향, 그 반대 방향일때는 제외 90도만 탐색
                    if d == before or d == op_di[before]:
                        continue
                    nnx,nny = nx+di[d][0],ny+di[d][1]
                    if is_valid(nnx,nny) and house[nnx][nny] != '*':
                        if visited[nnx][nny][d] > mirror:
                            visited[nnx][nny][d] = mirror+1
                            pq.append((mirror+1,d,nnx,nny))

    # 디버깅 코드=========================================================
    # for t in range(4):
    #     for r in visited:
    #         for c in r:
    #             if c[t] == INF:
    #                 print('.', end =' ')
    #                 continue
    #             print(c[t], end=' ')
    #         print()
    #     print(f'{t}===============')
    #=====================================================================
    return min(visited[end_x][end_y])

print(bfs(door))