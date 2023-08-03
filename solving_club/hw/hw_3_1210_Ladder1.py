T = 10
for t in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착 지점은 2 출발지점 1
    # 도착지점부터 출발 위로만 이동
    # 이동벡터
    # 숫자가 1인 경로를 따라 위쪽으로 가다 오른쪽이나 왼쪽에 1이 나오면 방향 전환환
    # 상 우 좌
    dr = [-1, 0, 0]
    dc = [0, 1, -1]
    # 초기 위치 = 값이 2인곳
    r = 99
    c = 0
    for col in range(100):
        if ladder[99][col] == 2:
            c = col
    nr, nc = 0, 0
    d = 0  # 이동방향 인덱스, 0 위, 1 오른쪽, 2 왼쪽
    while r > 0:
        nr = r + dr[d]
        nc = c + dc[d]

        # 올라가다는 상황일 때
        # 왼쪽 또는 오른쪽에 1 생기면 방향전환
        if d < 1:
            if 0 < c < 100 and ladder[r][c - 1] == 1:
                d = 2
                r = r + dr[d]
                c = c + dc[d]
            elif 0 <= c < 99 and ladder[r][c + 1] == 1:
                d = 1
                r = r + dr[d]
                c = c + dc[d]
            else:
                r, c = nr, nc
        # 왼쪽이나 오른쪽으로 가는 상황일 때
        # 위쪽에 1생기면 위로 방향 전환
        else:
            if ladder[r - 1][c] == 1:
                d = 0
                c = c + dc[d]
                r = r + dr[d]
            else:
                r, c = nr, nc

    print(f'#{tc} {c}')
