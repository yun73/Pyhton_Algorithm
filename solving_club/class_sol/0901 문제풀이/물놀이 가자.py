from collections import deque

def bfs(q):
    # 모든 물 시작점 탐색
    while q:
        # 현재 위치 반환
        r,c = q.popleft()
        # 현재 위치에서 상하좌우 탐색
        for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr = r + dr
            nc = c + dc
            # 범위 안에 있고 땅인 지역이면
            if 0<= nr < N and 0<=nc<M and wpark[nr][nc] == 'L':
                # 아직 탐색하지 않은 지역이면
                if visited[nr][nc] == 0 :
                    visited[nr][nc] = visited[r][c] + 1
                    # 연결된 곳 추가
                    q.append((nr,nc))
                else:
                    if visited[nr][nc] > visited[r][c] + 1:
                        # 더 작은 거리 값 들어오면 갱신해줘
                        visited[nr][nc] = visited[r][c] + 1
                        # 연결된 곳 추가
                        q.append((nr,nc))
                # 이미 들어있는 왕복 시간이 더 작거나 같으면 거기는 탐색하지 않을래
    return

T = int(input())
for tc in range(1,T+1):
    # N : 행 , M : 열
    N, M = map(int, input().split())
    wpark = [list(input()) for _ in range(N)]
    # 물이 있는 곳의 리스트
    water = deque()
    # 해당 땅의 물까지의 최소 이동 횟수 리스트
    visited = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            # 해당 위치가 물이면 다른 땅을 탐색하면서 거리 기록
            if wpark[r][c] == 'W':
                water.append((r,c))
    bfs(water)
    result = 0
    for line in visited:
        result += sum(line)

    print(f'#{tc} {result}')


