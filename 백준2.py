'''
미네랄
- 1초 / 128 MB

- 동굴 : RxC
    - 막대기 서로에게 던지며 소유권
    - 미네랑 저장, 막대기가 파괴함
    - 각 칸은 비어있거나 미네랄 이거나

- 클러스터
    - 네 방향 중 하나로 인접한 미네랄이 포함된 두 칸

- 창영(왼), 상근(오) : 던 번갈아가며 막대기 던짐

- 막대기가 미네랄을 만나면 그 칸의 미네랄은 모두 파괴되고 막대는 그 자리에서 이동 멈춤
    - 미네랄이 파괴후 클러스터가 분리가능
    - 새롭게 생성된 클러스터가 떠 있는 경우 - 중력에 의해 바닥으로

 두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다.
 클러스터가 떨어질 때, 그 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다.

1. 왼쪽 이면 상,하,우/ 오른쪽이면 상,하,좌 만 탐색

'''
from collections import deque

# 아래칸이 빈 경우, 벽을 넘는 경우에만 탐색해야 함
# 근데 맨 아래거만 해줘야 하니까 맨 아래인 경우를 찾아야 해
def dfs_down(sr,sc):
    cnt = 0
    for i in range(1,R+1):
        nr = sr + i * 1
        # 끝 넘어가면
        if nr == R:
            break
        # 다른 개체 만나면 끝
        if cave[nr][sc] == 'x':
            break
        cnt += 1

    return cnt


def bfs(sr,sc):
    global cave

    # 내릴 스택이랑, 내릴 거리
    # 내릴 거리는 위똑같이, 아래있으면 한칸 줄고, 오른쪽, 아래에 있으면 또 탐색
    stack = [(sr,sc)]
    # 각열당 가장 아래칸 인덱스 저장
    col = [-1]*C
    col[sc] = sr
    # 방문표시 및 해당 칸 아래 조사
    visited = [[0]*C for _ in range(R)]
    visited[sr][sc] = 1
    q = deque([(sr,sc)])
    # 최소거리만큼 내릴 수 있음
    min_dis = int(1e9)
    while q:
        # 현재 위치
        x,y = q.popleft()

        # 탐색 위치
        for i, di in enumerate(((1,0),(-1,0),(0,1),(0,-1))):
            nx,ny = x+di[0], y+di[1]
            if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
                # 이어진 클러스터의 경우

                if cave[nx][ny] == 'x':
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    stack.append((nx,ny))
                    # 해당 열의 최대 행값 갱신
                    col[ny] = max(col[ny],nx)
            # 만약 맨 바닥에 붙어있는 경우 내릴 수 없는 클러스터이므로 종료
            if nx == R:
                return False
    # 내려갈 수 있는 거리 조사/ 맨아래칸에서만
    for c_idx,row in enumerate(col):
        if row == -1:
            continue
        min_dis = min(min_dis,dfs_down(row,c_idx))

    # 만약 내릴수 있는 최소거리가 0이면 종료
    if min_dis == 0 or min_dis == int(1e9):
        return False
    print(min_dis)
    # 내리는 로직
    # 스택에 들어있는 모든 좌표를 최소거리만큼 내리자
    print(stack.sort())
    for a,b in stack:
        cave[a][b] = '.'
        cave[a+min_dis][b] = 'x'

    return True



R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
stick = list(map(int, input().split()))

for i in range(N):
    throw = R - stick[i]
    if not i%2:
        # 왼쪽 창영
        for j in range(C):
            if cave[throw][j] == '.':
                continue
            # 미네랄 발견하면 파괴
            cave[throw][j] = '.'
            for di in ((1,0),(-1,0),(0,1)):
                nt,nj = throw + di[0],j+di[1]
                if 0<=nt<R and 0<=nj<C and cave[nt][nj]=='x':
                    result = bfs(nt, nj)
                    if result:
                        break
            break

    else:
        # 오른쪽 상근
        for j in range(C-1,-1,-1):
            if cave[throw][j] == '.':
                continue
            # 미네랄 발견하면 파괴
            cave[throw][j] = '.'
            for di in ((1, 0), (-1, 0), (0, -1)):
                nt, nj = throw + di[0], j + di[1]
                if 0 <= nt < R and 0 <= nj < C and cave[nt][nj]=='x':
                    result = bfs(nt, nj)
                    if result:
                        break
            break

    for line in cave:
        print(''.join(line))
    print('=================')


for line in cave:
    print(''.join(line))

