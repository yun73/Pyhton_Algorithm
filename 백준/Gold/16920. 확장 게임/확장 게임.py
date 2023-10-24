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

def bfs(now, player):
    global count

    new_castle = deque()
    while now:
        x,y = now.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and not visited[nx][ny] and land[nx][ny] == '.':
                new_castle.append((nx, ny))
                visited[nx][ny] = player
                count[player] += 1

    return new_castle


N, M, P = map(int, input().split())
S = [0] + list(map(int, input().split()))
land = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
count = [0] * (P + 1)
castle = [deque() for _ in range(P+1)]
for r in range(N):
    for c in range(M):
        if land[r][c] != '#' and land[r][c] != '.':
            p = int(land[r][c])
            castle[p].append((r,c))
            visited[r][c] = p
            count[p] += 1

res = 1
while res:
    res = 0
    for player in range(1,P+1):
        for dis in range(1,S[player]+1):
            if not castle[player]:
                break
            castle[player] = bfs(castle[player],player)
        else:
            res = 1

count.pop(0)
print(*count)
