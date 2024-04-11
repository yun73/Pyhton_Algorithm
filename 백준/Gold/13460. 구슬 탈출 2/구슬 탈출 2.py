import sys
input = sys.stdin.readline

di = [(1,0),(0,1),(-1,0),(0,-1)]

def move_select(idx,red,blue):
    if idx == 0:
        if red[0] >= blue[0]:
            return 'red'
        else:
            return 'blue'
    elif idx == 1:
        if red[1] >= blue[1]:
            return 'red'
        else:
            return 'blue'
    elif idx == 2:
        if red[0] <= blue[0]:
            return 'red'
        else:
            return 'blue'
    elif idx == 3:
        if red[1] <= blue[1]:
            return 'red'
        else:
            return 'blue'

def moving(dx,dy,color,op_color):
    dis_range = 0
    if dx != 0:
        dis_range = N-2
    else:
        dis_range = M-2

    for dis in range(1,dis_range+1):
        nx,ny = color[0] + dis*dx , color[1]+dis*dy
        if board[nx][ny] == '#' or ((op_color[0],op_color[1]) != (point['O'][0],point['O'][1]) and (nx,ny) == (op_color[0],op_color[1])):
            return [color[0] + (dis-1)*dx , color[1]+(dis-1)*dy]
        if [nx,ny] == point['O']:
            return [nx,ny]


def bt(cnt, red,blue): # 현재 움직인 횟수와 각 현재 정보
    global res

    if cnt >= 11:
        return

    if blue == point['O']:
        return
    if red == point['O']:
        res = min(res,cnt)
        return

    for idx,(dx,dy) in enumerate(di):
        ans = move_select(idx,red,blue)
        if ans == 'red':
            new_red = moving(dx,dy,red,blue)
            new_blue = moving(dx,dy,blue,new_red)
        else:
            new_blue = moving(dx,dy,blue,red)
            new_red = moving(dx,dy,red,new_blue)

        if new_red == red and new_blue == blue:
            continue

        bt(cnt+1,new_red,new_blue)


N,M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

point = {'R':[0,0], 'B':[0,0], 'O':[0,0]}

for r in range(N):
    for c in range(M):
        if board[r][c] == '#' or board[r][c] == '.':
            continue
        point[board[r][c]] = [r,c]
        board[r][c] = '.'


res = 11
bt(0,point['R'],point['B'])

if res == 11:
    print(-1)
else:
    print(res)
