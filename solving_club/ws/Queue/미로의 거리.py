# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_start(N, maze):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c


def is_valid(nr, nc):
    if 0 <= nr < N and 0 <= nc < N:
        return True
    else:
        return False


def bfs(sr, sc):
    # 방문 기록
    visited = [[0] * N for _ in range(N)]
    que = []
    # 인큐로 현재 위치 저장해두자
    que.append((sr, sc))
    # 현재 위치 벽으로 바꿔주자
    visited[sr][sc] = 1
    # 벽으로 바꿔 줘도 다음 모든 경로 저장해둬서 탐색하니까 괜찮음
    while que:  # 큐가 다 비면 모든 곳을 탐색했다는 것
        # 현재 위치반환
        r, c = que.pop(0)
        # 현재 위치와 인접한 지역 찾기
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                # 갈 수 있는 위치이면 que에 추가
                que.append((nr, nc))
                # 방문기록도 남기자 근데 지금까지 몇개 거쳐서 왔는지도
                visited[nr][nc] = visited[r][c] + 1
                # 근데 목표 지점에 도달했으면 얼마나 걸렸는지 반환하지
                if maze[nr][nc] == 3:
                    return visited[nr][nc] - 2

    # 다 탐색 했는데도 안에서 3 인 지점 못 찾고 나오면
    return 0


T = int(input())
for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())
    # 미로 정보 입력 받기
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발점 찾아서 입력 받기
    sr, sc = find_start(N, maze)

    print(f'#{tc} {bfs(sr, sc)}')