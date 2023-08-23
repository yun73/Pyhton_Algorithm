# 모든방향 자기 자신과 다른돌 탐색할 델타 시계방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

T = int(input())
for tc in range(1, T + 1):
    # N : 보드 한변의 길이, M : 돌을 놓는 횟수
    N, M = map(int, input().split())
    # 흑돌 : 1, 백돌 : 2
    # 보드 만들기
    board = [[0] * N for _ in range(N)]
    # 시작돌 놓기
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2

    # 돌 놓기
    for _ in range(M):
        r, c, color = map(int, input().split())
        r -= 1
        c -= 1
        print(r, c, color)
        # 일단 현재 위치에 돌을 두자
        board[r][c] = color
        # 돌을 놓을 수 있는 곳은 다른색을 같은색과 끼고 있는 곳이다

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            between = []
            # 해당 방향에 색깔이 다른게 있을 때 그 건너에 나랑 같은 거 있는지 확인하고
            # 발견하면 그 사이의 검은색들 모두 하얀색으로 바꾸기
            while 0 <= nr < N and 0 <= nc < N and board[nr][nc] != 0:
                # 만약 나랑 같은 숫자 발견하면
                if board[nr][nc] == color:
                    # 스택에 저장된 위치의 색깔을 내 색깔과 같게 만들자
                    while between:
                        i, j = between.pop()
                        # 내 색깔로 변경
                        board[i][j] = color
                    break  # 이거로 빠져나가면 else 구문 실행 안됨
                # 사이의 다른색깔 돌들 위치 저장
                between.append((nr, nc))
                nr += dr[d]
                nc += dc[d]


        for i in range(N):
            for j in range(N):
                if board[i][j] == 2:
                    print('W', end=' ')
                elif board[i][j] == 1:
                    print('B', end=' ')
                else:
                    print('.', end=' ')
            print()
        print('========')

    # 돌 다 놨으면
    # 이제 남은 돌의 개수를 세주자
    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                white += 1
            elif board[i][j] == 1:
                black += 1

    print(f'#{tc} {black} {white}')
