dr = [0, 1, 1, 1, 0]
dc = [-1, -1, 0, 1, 1]

# def kill(r,c):
#     global dr
#     global dc
#     global board
#     # 놓게 되는 순간 다음에 못놓게 되는곳 -1로 만들기
#     # 왼 왼대 아 오대 오
#     for d in range(5):  # 제거할 방향
#         nr = r + dr[d]
#         nc = c + dc[d]
#         while 0 <= nr < N and 0 <= nc < N:
#             if board[nr][nc] != -1:
#                 board[nr][nc] = -1
#                 nr += dr[d]
#                 nc += dc[d]
#     return

def queen(r, N):
    global board
    global possible

    if r == N:
        for zero in board[r-1]:
            if zero == 0:
                possible += 1

    else:
        for c in range(N):
            stack = []
            if board[r][c] == 0:
                # 놓게 되는 순간 다음에 못놓게 되는곳 -1로 만들기
                # 왼 왼대 아 오대 오
                for d in range(5):  # 제거할 방향
                    nr = r + dr[d]
                    nc = c + dc[d]
                    while 0 <= nr < N and 0 <= nc < N:
                        stack.append((nr,nc))
                        board[nr][nc] = -1
                        nr += dr[d]
                        nc += dc[d]
                queen(r+1, N)
                # 초기화
                while stack:
                    kr,kc = stack.pop()
                    board[kr][kc] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N*N 크기의 보드판 생성
    board = [[0] * N for _ in range(N)]
    # print(board)
    # 놓을 수 있는 경우의 수
    possible = 0

    r = 0
    queen(r, N)
    print(f'#{tc} {possible}')
