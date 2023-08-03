# 달팽이가 1부터 N*N 까지의 숫자 시계방향
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 전체 채워야할 숫자는 1~ N^2
    # 방향 전환 무조건 오른쪽으로 만
    # 시작 위치 r, c
    # 진행방향 인덱스
    d = 0
    # 오0 아래1 왼2 위3
    move = 1
    # 시작위치
    r, c = 0, 0
    # 움직일위치
    nr, nc = 0, 0

    # 총 15번 움직여야함
    while move < N * N + 1:
        snail[r][c] = move
        nr = r + dr[d]
        nc = c + dc[d]
        # 아래로 가야될 때 유효 범위내 없으 d
        if (0 <= nr < N and 0 <= nc < N) and snail[nr][nc] == 0:
            r, c = nr, nc

        else:
            d = (d + 1) % 4
            r = r + dr[d]
            c = c + dc[d]

        move += 1

    print(f'#{tc}')
    for n in range(N):
        print(*snail[n])


# 강사님 풀이

T = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    # 달팽이집 채우기 (0,0) 고정
    # N *N 번 반복하며 채우기
    # 우 하 좌 상
    d = 0  # 채워 나가는 방향
    # 시작위치
    r, c = 0, 0
    for i in range(1, (N * N) + 1):
        snail[r][c] = i
        # 다음 방향으로 진행
        # 다음 위치가 유효한 지 확인
        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 위치가 유효하지 않으면
        if (0 <= nr < N and 0 <= nc < N) and snail[nr][nc] == 0:
            # 인덱스 에러 발생할 수 있으니까 인덱스에 넣을 값 먼저 조건 문 앞에 오게
            # 다음 위치가 유효하면 계속 가고
            r, c = nr, nc
        else:
            # 유효하지 않으면 방향 꺽기
            # if d < 3:
            #     d = d + 1
            # else:
            #     d = 0
            d = (d + 1) % 4
            r = r + dr[d]
            c = c + dc[d]

    print(f'#{tc}')
    for n in range(N):
        print(*snail[n])
