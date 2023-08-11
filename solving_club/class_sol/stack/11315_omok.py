#    우 대 아 대 왼  시계방향 탐색
# 현재 위치에서 상하좌우 대각선에 o 돌 존재하면 그 자리로 찾아가서 끝까지 탐색
# 탐색하면서 방문했다고 표시하는데 해당 위치 주변에 아직 다른
# 위쪽은 탐색할 필요가 없어 어짜피 위에서 다 확인 함
def omok(board, N, dr, dc):
    # 현재 위치
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':  # 돌멩이가 있을 때
                for i in range(5):
                    cnt = 1
                    nr = r + dr[i]
                    nc = c + dc[i]
                    while True:  # 현재 위치 기준 한방향으로 이동 시작

                        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 'o':
                            # 조건 만족하면 해당 방향으로 이동
                            cnt += 1
                            nr += dr[i]
                            nc += dc[i]

                        else:  # 돌멩이를 못찾으면
                            break

                    if cnt >= 5:
                        return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    dr = [0, 1, 1, 1, 0]
    dc = [1, 1, 0, -1, -1]

    print(f'#{tc} {omok(board, N, dr, dc)}')
