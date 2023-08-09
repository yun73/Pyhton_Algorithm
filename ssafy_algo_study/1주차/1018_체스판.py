# 8 * 8 크기의 두가지 케이스의 체스판 미리 만들어두기
black = 'BWBWBWBW'
white = 'WBWBWBWB'


N, M = map(int, input().split())
board = [input() for _ in range(N)]
for n in range(N):
    for m in range(M-8+1):
        for i in range(8):
            for j in range(8):
                if board[n][m+j] != board_B[i][j]:
                    count_b += 1

                if board[n+i][m+j] != board_W[i][j]:
                    count_a += 1