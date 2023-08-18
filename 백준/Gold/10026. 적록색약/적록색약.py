# 적록색약
# R G B
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(nr, nc):
    if 0 <= nr < N and 0 <= nc < N:
        return True
    else:
        return False


def bfs(cw):
    area = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                visited[r][c] = 1
                que = []
                color = picture[r][c]
                if cw == 1: # 색맹인 경우에는
                    if picture[r][c] == 'B': # 파란색인 경우는 파란색 영역만 탐색
                        que.append((r,c))
                        while que:
                            i, j = que.pop(0)
                            for d in range(4):
                                nr = i + dr[d]
                                nc = j + dc[d]
                                if is_valid(nr, nc) and picture[nr][nc] == color and not visited[nr][nc]:
                                    que.append((nr,nc))
                                    visited[nr][nc] = 1
                        area += 1


                    else: # 초록색이나 빨간색 발견하면 해당 영역 탐색
                        que.append((r, c))
                        while que:
                            i, j = que.pop(0)
                            for d in range(4):
                                nr = i + dr[d]
                                nc = j + dc[d]
                                if is_valid(nr, nc) and picture[nr][nc] in ['R', 'G'] and not visited[nr][nc]:
                                    que.append((nr, nc))
                                    visited[nr][nc] = 1
                        area += 1
                if cw == 0:  # 색맹이 아닌
                    que.append((r, c))
                    while que:
                        i, j = que.pop(0)
                        for d in range(4):
                            nr = i + dr[d]
                            nc = j + dc[d]
                            if is_valid(nr, nc) and picture[nr][nc] == color and not visited[nr][nc]:
                                que.append((nr, nc))
                                visited[nr][nc] = 1
                    area += 1

    return area




N = int(input())
picture = [list(input()) for _ in range(N)]
area = 0
print(bfs(0), bfs(1))