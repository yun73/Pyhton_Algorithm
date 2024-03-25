'''
지도 N X M

지도 칸 0 이면 주사 위 값이 복사
0이 아니면 칸에 쓰인 수가 주사위 바닥으로 복사 > 칸에 쓰인 수는 0

주사위가 이동할 때 마다 상단에 쓰여있는 값

'''
import sys
input = sys.stdin.readline

di = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} # 동 서 북 남

dice = {'top':0,'bottom':0,'e':0, 'w':0,'n':0, 's':0}

def go(arrow):
    if arrow == 1: # 동
        dice['top'], dice['bottom'], dice['e'], dice['w'] = dice['w'], dice['e'], dice['top'], dice['bottom']
    elif arrow == 2: # 서
        dice['top'], dice['bottom'], dice['e'], dice['w'] = dice['e'], dice['w'], dice['bottom'], dice['top']
    elif arrow == 3:  # 북
        dice['top'], dice['bottom'], dice['n'], dice['s'] = dice['s'], dice['n'], dice['top'], dice['bottom']
    elif arrow == 4: # 남
        dice['top'], dice['bottom'], dice['n'], dice['s'] = dice['n'], dice['s'], dice['bottom'], dice['top']




N, M, x, y, K = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
command = list(map(int,input().split()))

now_x,now_y = x,y
for k in command:
    # print('명령',k)
    # 이동 시키려는 다음 위치
    next_x,next_y= now_x + di[k][0], now_y + di[k][1]
    # 밖으로 이동시키려는 경우 무시
    if not(0 <= next_x < N and 0 <= next_y < M):
        continue
    # 움직임 구현
    go(k)
    now_x, now_y = next_x, next_y
    # 만약 이동한 칸 바닥 0
    if board[next_x][next_y] == 0:
        # 주사위 바닥 수 복사
        board[next_x][next_y] = dice['bottom']
    else:
        # 칸의 수 주사위 바닥에 복사
        dice['bottom'] = board[next_x][next_y]
        # 칸의 수 0으로 초기화
        board[next_x][next_y] = 0
    # 출력
    print(dice['top'])

