# 상하좌우 탐색
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def find_start(maze):
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                return r, c


def bfs(sr, sc, maze):
    # 큐 생성
    Q = []
    # 현재 위치 인큐
    Q.append((sr, sc))
    # 현재 위치 다시 탐색 못하게 벽으로 만들어주자
    maze[sr][sc] = 1

    while Q:  # 큐가 빌 때 까지 돌기
        r, c = Q.pop(0)  # 현재 위치 반환
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 16 and 0 <= nc < 16 and maze[nr][nc] != 1:
                Q.append((nr, nc))  # 다음에 탐색할 길에 추가

                if maze[nr][nc] == 3:
                    return 1
                else:
                    maze[nr][nc] = 1

    # 길찾아가다 전부다 돌았을 때 탈출 못하면 걍로 없으니까 0 출렬
    return 0


T = 10
for tc in range(1, T + 1):
    int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    sr, sc = find_start(maze)

    print(f'#{tc} {bfs(sr, sc, maze)}')
