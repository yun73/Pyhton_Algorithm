# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def start(maze):  # 시작점찾기
    sp = 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r,c


def find_exit(N, maze):
    # 방문하면 다시 안방문할
    visited = [[0] * N for _ in range(N)]
    stack = []

    r, c = start(maze)
    # 출발 지점 방문 표시
    visited[r][c] = 1
    while True:
        if maze[r][c] == 3:
            return 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                # 다음 위치 탐색 성공하면
                # 현재 위치를 스택에 추가
                stack.append((r, c))
                # 다음 위치 정보로 갱신
                r, c = nr, nc
                # 다음 위치 방문할 거니까 표시
                visited[r][c] = 1
                break  # 이동하고 전위치에서 탐색하는게 아니라 다음위치에서 탐색해야 하니까 다음 반복으로

        else:  # 만약 이동 방향 모두 막혀 있으면 스택에 저장되어 있는 이전 저장 위치로 이동
            if stack:  # 스택에 값이 있으면
                r, c = stack.pop()
            else:  # 모든 방문 끝나서 값이 없으면
                break
    # 출구 못찾고 미로찾기 끝나면
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {find_exit(N, maze)}')