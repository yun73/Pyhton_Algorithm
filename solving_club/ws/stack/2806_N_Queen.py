dr = [0, 1, 1, 1, 0]
dc = [-1, -1, 0, 1, 1]

#
# def queen(r, N):
#     global possible
#     # 죵료 조건
#     if r == N:
#         possible += 1
#     # 재귀 호출
#     # 퀸 위치가 board[][] = 1 이런식으로 위치시키자
#     # 못 놓게 되는 곳은 board[][] = -1
#     else:
#         for c in range(N):
#             # if 0 not in board[r]:
#             #     return
#             stack = [0]*N*N
#             top = -1
#             if board[r][c] < 1:
#                 # board[r][c]  # r행 에서 퀸을 놓게 되면
#                 # 놓게 되는 순간 다음에 못놓게 되는곳 -1로 만들기
#                 # 왼 왼대 아 오대 오
#                 for d in range(5):  # 제거할 방향
#                     nr = r + dr[d]
#                     nc = c + dc[d]
#                     while 0 <= nr < N and 0 <= nc < N:
#                         top += 1
#                         stack[top] = (nr,nc)
#                         board[nr][nc] += 1
#                         nr += dr[d]
#                         nc += dc[d]
#                 # 제거된 상태에서 다음 퀸 놓으로 출발
#                 queen(r + 1, N)
#                 # 초기화
#             while top>-1:
#                 kr, kc = stack[top]
#                 top -= 1
#                 board[kr][kc] -= 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     # N*N 크기의 보드판 생성
#     board = [[0] * N for _ in range(N)]
#     # print(board)
#     # 놓을 수 있는 경우의 수
#     possible = 0
#
#     r = 0
#     queen(r, N)
#     print(f'#{tc} {possible}')


def gqueen(r, N, col, ld, rd):
    global possible
    if r == N:
        possible += 1
    else:
        for c in range(N):
            if (col[c] or ld[r - c + N - 1] or rd[r + c]):
                continue

            col[c] = ld[r - c + N - 1] = rd[r + c] = True
            gqueen(r + 1, N, col, ld, rd)
            col[c] = ld[r - c + N - 1] = rd[r + c] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    possible = 0

    col = [False] * N
    ld = [False] * (2 * N - 1)
    rd = [False] * (2 * N - 1)

    gqueen(0, N, col, ld, rd)
    print(f'#{tc} {possible}')
