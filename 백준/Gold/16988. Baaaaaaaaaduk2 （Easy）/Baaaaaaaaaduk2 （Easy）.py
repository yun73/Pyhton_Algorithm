'''

한번에 2개 씩 놔둘 수 있는 바둑
- 두 개 놔서 원래는 죽는 위치지만 상대를 죽일수도 있음

현재 판이 주어졌을 때 돌 2개 둬서 죽일 수 있는 상대 돌의 최대 개수

0:빈칸
1:내돌
2:AI

상대방 돌을 탐색해서
인접한 곳 중에 빈칸이 2곳 이하면 가능
    - 이때 해당 돌의 좌표를 기록
마지막에 최대 개수 세주기
'''
import sys
input= sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
possible = {0:{},1:{},2:{}}
for r in range(N):
    for c in range(M):
        if board[r][c] < 2 or visited[r][c]:
            continue
        # ai 돌이면 bfs 탐색 시작
        q = [(r,c)]
        visited[r][c] = 1
        cnt = 1
        # 돌다가 인접한 빈칸의 좌표
        blank = []
        while q:
            x,y = q.pop(0)
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if not(0 <= nx < N and 0<= ny < M) or board[nx][ny] == 1 or visited[nx][ny]:
                    continue
                # 만약 빈칸이면
                if board[nx][ny] == 0:
                    blank.append((nx,ny))
                    continue
                # 나랑 같은 돌이면
                visited[nx][ny] = 1
                cnt += 1
                q.append((nx,ny))
        blank = list(set(blank))
        # 이어져있는 2 의 개수와 인접한 빈칸 정보가 있음
        blank.sort()
        if len(blank) <= 2:
            possible[len(blank)].setdefault(str(blank).rstrip(']').lstrip('['),0)
            possible[len(blank)][str(blank).rstrip(']').lstrip('[')] += cnt

# print(possible)
max_cnt = 0
cnt_0 = 0
if possible[0]:
    cnt_0= sum(possible[0].values())
    max_cnt= max(max_cnt,cnt_0)

if possible[1]:
    if len(possible[1]) == 1:
        max_cnt = max(max_cnt, cnt_0 + list(possible[1].values())[0])
    elif len(possible[1]) >= 2:
        tmp = sorted(list(possible[1].values()))
        max_cnt = max(max_cnt, cnt_0 + tmp[-1] + tmp[-2])

    for key1, value in possible[1].items():
        for key2 in possible[2]:
            if key1 in key2:
                possible[2][key2] += value

cnt_2 = 0
if possible[2]:
    cnt_2 = max(list(possible[2].values()))
    max_cnt = max(max_cnt,cnt_0 + cnt_2)

print(max_cnt)

