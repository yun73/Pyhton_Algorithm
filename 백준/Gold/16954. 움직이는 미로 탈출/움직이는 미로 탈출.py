'''
움직이는 미로탈출

- 체스판 : 8x8
    - 빈칸 : '.'
    - 벽 : '#'
        - 1초마다 아래 행으로 이동
        - 가장 아래행인 경우 벽 사라짐

- 욱제 가장 아래칸 : (7,0)

- 탈출 : 가장 오른쪽 윗칸 (0,7)

- 이동
    - 1초에 인접한 8방향 가능
    - 가만히 있는 것도 가능
    - 빈칸으로만 이동 가능

- 욱제 먼저 움직으로, 그다음 벽이 움직임

- 욱제 탈출할 수 있을 까?

- 벽은 욱제의 이동과 상관없이 계속 내려온다
- 벽이 캐릭터 있는 칸으로 이동하면 더이상 캐릭터는 이동 불가
- 가상벽을 만들어 다음 이동시 벽에 부딪히는 곳이면 가지 말자
- 그냥 탐색시 해당칸의 위칸에 벽이 있으면 가지 말자


- 벽을 한줄씩 내려오므로 8번 내려오면 벽이 다 사라진다
- 벽 내리는 걸 맨 위에 한줄씩 추가하게 되면 알아서 캐릭터의 위치는 그대로고 벽 위치만 바뀐다
'''
import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(8)]
pq = deque()
pq.append((7,0))
cnt = 0
res = 0
while pq:
    # 도착했으면 종료
    if res == 1:
        break
    # 벽 8번 밀어냈으면 종료
    if cnt >= 8:
        res = 1
        break

    # 현재 위치에서 갈수 있는 곳 탐색해서 넣어주기
    for _ in range(len(pq)):
        x,y = pq.popleft()
        # 종료지점 찾으면 종료
        if (x,y) == (0,7):
            res = 1
            break

        for nx in range(x-1,x+2):
            for ny in range(y-1,y+2):
                if 0<=nx<8 and 0<=ny<8 and board[nx][ny] == '.':
                    # 이동할 위치의 위에가 벽이면 거기로 이동하지마
                    if nx-1 >= 0 and board[nx-1][ny] =='#':
                        continue
                    pq.append((nx,ny))

    # 벽 밀어내기
    board = [['.'] * 8] + board
    cnt += 1

print(res)


