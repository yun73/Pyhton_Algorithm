import sys

sys.stdin = open("input.txt", "r")

T = 10
N = 100

# 사다리타기 게임의 규칙
# 상하 방향으로 가는데 중간에 좌우 방향에 길이 있으면 좌우 부터
dr = [0, 0, -1]
dc = [-1, 1, 0]

for tc in range(1, T + 1):
    int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]

    # 내가 위치를 직접 움직여야 한다.
    # 행번호
    r = 99
    # 열번호
    c = -1  # 마지막행 검사를 해서 2인곳을 찾을거다.

    # 2라고 표시된 곳을 마지막 줄에서 찾기
    for i in range(N):
        if ladder[99][i] == 2:
            c = i

    # 우리가 거슬러 올라갈 시작 위치 찾음
    # (r,c)
    d = 2
    # 왼쪽 0 오른쪽 1 위쪽 2

    while r > 0:
        # 이동할 때마다 좌우상 순서로 탐색
        for d in range(3):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음위치가 유효한 인덱스인지 검사
            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1:
                # 갈수 있으면 간다.
                # 현재위치 갱신
                r = nr
                c = nc
                # 내가 왔던길 다시 보지 ㅇ낳도록 0으로 바꾼다.
                ladder[r][c] = 0
                # 길을 찾았으니까 더 필요 없음
                break

    # 반복문이 끝나면 r 이 0이 되었을 거니까 출력

    print(f'{tc} {c}')
