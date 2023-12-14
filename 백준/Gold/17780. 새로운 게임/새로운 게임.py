'''
새로운 게임
'''
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [1,-1,0,0]
di = {0:1,1:0,2:3,3:2} # 반대방향

def move(i,from_blue):
    global check
    x,y = unit[i]
    # 이동하는 말의 위치의 첫번째 말과 일치하면 이동
    if unit_in_board[x][y][0][0] != i:
        return
    go = unit_in_board[x][y][0][1]
    # 첫번째 말의 이동방향에 따라 이동
    nx,ny = x+dx[go], y + dy[go]
    if not(0<=nx<N and 0<=ny<N):
        if not from_blue:
            go_op = di[go]
            unit_in_board[x][y][0][1] = go_op
            move(i,True)

        return
    # 흰색
    if board[nx][ny] == 0:
        while unit_in_board[x][y]:
            unit_i = unit_in_board[x][y].pop(0)
            unit[unit_i[0]] = [nx, ny]
            unit_in_board[nx][ny].append(unit_i)
    # 빨간색
    elif board[nx][ny] == 1:
        while unit_in_board[x][y]:
            unit_i = unit_in_board[x][y].pop()
            unit[unit_i[0]] = [nx,ny]
            unit_in_board[nx][ny].append(unit_i)
    # 파랑색
    elif board[nx][ny] == 2:
        if not from_blue:
            go_op = di[go]
            unit_in_board[x][y][0][1] = go_op
            move(i,True)
        else:
            return

    # 말 4개 이상 시 종료
    if len(unit_in_board[nx][ny]) >= 4:
        check = True

    return


# N: 체스판 크기 ,K: 말의 개수
N,K = map(int, input().split())
# 체스판 정보 ( 0:하양,1:빨강,2:파랑)
board = [list(map(int, input().split())) for _ in range(N)]
unit_in_board = [[[] for _ in range(N)] for _ in range(N)]

unit = [0]*(K+1)
for i in range(1,K+1):
    x,y,go = map(int,input().split())
    unit[i] = [x-1,y-1]
    unit_in_board[x-1][y-1].append([i,go-1])
# print(unit_in_board)
check = False
turn = 1
while True:
    if turn > 1000:
        print(-1)
        break

    for i in range(1,K+1):
        move(i,False)

    if check:
        print(turn)
        break

    turn += 1

