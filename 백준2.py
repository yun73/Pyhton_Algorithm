'''
확장 게임

- 땅 : N x M

- 각 플레이어는 하나 이상의 성을 가짐

- 성 확장 : 플레이어 i는 자신이 있는 곳에서 Si 만큼 이동할 수 있는 모든 칸에 성을 동시에 만듦
- 상하좌우 가능
- 턴 돌아가면서 확장
- 모든 플레이어 확장 풀가능하면 게임 끝

- 턴마다 내가가지고 있는 성의 위치에서 bfs 를 si칸 만큼 탐색 가능
- 턴마다 bfs 탐색을 하면 시초날 거 같은데
'''
import sys
from collections import deque

input = sys.stdin.readline


def is_valid(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    return False


def bfs(castle):
    global visited
    global count
    player = 1
    # 현재 가지고 있는 영역을 다 탐색할 때 까지 반복
    while True:

        i, j = castle[player].popleft()
        q = deque()
        q.append((i, j))
        while q:
            player, x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                # 요효 범위이며
                if is_valid(nx, ny) and land[nx][ny] == '.':
                    if 1 <= abs(nx-i)+abs(ny-j)<=S[player]:
                        if visited[nx][ny]:
                            continue
                        # 방문처리
                        visited[nx][ny] = 1
                        count[player] += 1

                        # 만약 가장자리면
                        if abs(nx-i)+abs(ny-j)==S[player]:
                            castle.append((nx,ny))
                        else:
                            q.append((nx, ny))


N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
land = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
count = [0] * (P + 1)
castle = [[]*(P+1)]
for r in range(N):
    for c in range(M):
        if land[r][c] != '#' and land[r][c] != '.':
            castle[int(land[r][c])].append((r, c))
            count[int(land[r][c])] += 1
            visited[r][c] = int(land[r][c])

bfs(castle)
count.pop(0)
print(*count)
