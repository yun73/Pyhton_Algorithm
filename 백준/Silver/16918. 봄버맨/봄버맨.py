import sys
input = sys.stdin.readline
from collections import deque

di = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(q,board):
    while q:
        x,y = q.popleft()
        board[x][y] = '.'
        for i in range(4):
            nx,ny = x+di[i][0],y+di[i][1]
            if 0<= nx<R and 0 <= ny<C and board[nx][ny] == 'O':
                board[nx][ny] = '.'

def plant_bomb(t):
    global q, board
    if t == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    elif t%2 == 1: # 3초가 지난 폭탄 폭발
        bfs(q,board)
        # 3초후에 터질 폭탄을 q에 다시 저장한다.
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    q.append((i,j))
    else:
        board = [['O']*C for _ in range(R)]

R,C,N = map(int,input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]
q = deque()

for i in range(1,N+1):
    plant_bomb(i)

for i in board:
    print(''.join(i))