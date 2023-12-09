'''
방문한 곳을 다시 방문하는 경우도 있음
dfs
'''
import sys

input = sys.stdin.readline

di = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back = {0: 2, 1: 3, 2: 0, 3: 1}

N, M = map(int, input().split())

sr, sc, sd = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

def clean_dfs(sx, sy,sd):

    cnt = 1
    visited[sx][sy] = 1
    q = []
    q.append((sx,sy,sd))

    while q:
    # 현재 방향기준으로 반시게 방향으로 탐색
        x,y,d = q.pop(0)
        for dr in range(4):
            direction = (3 - (dr - d)) % 4
            dx, dy = di[direction]
            nx, ny = x + dx, y + dy
            # 만약 청소되지 않은 빈칸 있으면
            if 0 <= nx < N and 0 <= ny < M and not room[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny,direction))
                cnt += 1
                break
        # 주변4칸 중에 청소되지 않은 빈칸이 없는 경우
        else:
            # 바라보는 방향 유지할 채로 한 칸 후진
            dx, dy = di[back[d]]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if room[nx][ny]:
                    return cnt
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1

                q.append((nx,ny,d))


print(clean_dfs(sr, sc, sd))