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

def is_valid(x,y):
    if 0<=x<N and 0 <=y<M:
        return True
    return False

def bfs(player):

    visited = [[0]*M for _ in range(N)]
    count = [[0]*(P+1)]
    for p in range(1,P+1):
        new_player = deque()
        # 현재 가지고 있는 영역을 다 탐색할 때 까지 반복
        while player[p]:
            x,y = player[p].popleft()
            count[p] += 1

            for dx,dy in ((),(),(),()):
                for dis in range(S[p],0,-1):
                    nx,ny = x+dx*dis, y+dy*dis
                    if is_valid(nx,ny) and not visited[nx][ny]:
                        visited[nx][ny] = p





        else:
            player[p] = new_player




N,M,P = map(int,input().split())
S = [0] + list(map(int, input().split()))
land = [list(input()) for _ in range(N)]

player = [deque([])*(P+1)]
for r in range(N):
    for c in range(M):
        if land[r][c] != '#' and land[r][c] != '.':
            player[int(land[r][c])].append((r,c))

bfs(player)



