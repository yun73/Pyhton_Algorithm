'''
마법사 상어와 비바라기 - 파이어볼, 토네이도, 파이어스톰, 물복사버그 마법
비바라기 시전시 하늘에 비구름 생성 가능

'''
# 비바라기 연습
# NxN 크기의 격자에서
# 격자의 각 칸에 바구니 하나 있음
# r행c열 의 바구니 (r,c) , 해당바구니의 물의 양 A[r][c]
# (1,1) ~ (N,N) 행열 시작과 끝 연결
# 행열 모드 연산?
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
di = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
# 물복사하는 범위
dcopy = [[-1, -1], [1, 1], [-1, 1], [1, -1]]


def move(d, s, cloud, N):
    # 구름들의 좌표를 이동방향으로 거리만큼 옮기고
    # 이동하는 경우 두가지
    for r, c in cloud:
        nr = r + s * di[d][0]
        nc = c + s * di[d][1]
        # 다음 위치 판단하,고 만들어줄 좌표
        dis_r, dis_c = 0, 0
        # 행 열 좌표 따로 판단
        # 범위 안에 있을 때는 그냥 이동
        # N 넘어갈 때는 mod 연산 해주면 됨
        # 1 아래로 갈 때는 N-1 - 나머지연산 결과
        # 행
        if 0 <= nr < N:  # 범위 안에 있을 때
            dis_r = nr
        elif nr >= N:  # N 넘을때
            dis_r = nr % N
        elif nr < 0:  # 0 아래로
            if abs(nr) % N != 0:
                dis_r = N - abs(nr) % N
            else:
                dis_r = 0
        # 열
        if 0 <= nc < N:
            dis_c = nc
        elif nc >= N:  # N 넘을때
            dis_c = nc % N
        elif nc < 0:  # 0 아래로
            if abs(nc) % N != 0:
                dis_c = N - abs(nc) % N
            else:
                disc = 0
        # 그 자리에 1만큼 비 내려주고
        A[dis_r][dis_c] += 1
        # 해당 위치를 즉 구름이 사라지는 위치를 discloud에 저장해줘야함
        discloud.append((dis_r, dis_c))


def water_copy_bug(discloud):
    # 구름이 사라진 지점 = 바구니 물 양 증가한 지점
    for r, c in discloud:
        # 대각선 방향 탐색
        for dr, dc in dcopy:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if A[nr][nc] != 0:
                    A[r][c] += 1


# 대각선 방향으로 거리 1인 칸의 물의 양만큼 현재 바구니의 물의 양 증가
# 이때 경계 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다
# 즉 이동 시에는 각 행열의 모서리 부분에서 순환하지만 대각선 탐색은 경계까지만

N, M = map(int, input().split())
# [[0] for _ in range(N + 1)] +
A = [list(map(int, input().split())) for _ in range(N)]
# i 번째 이동명령 방향 di, 거리 si 로 이루어짐
info = [list(map(int, input().split())) for _ in range(M)]
# 비바라기 시전
#  (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생김
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
# 다음 구름 생성시 이전 구름 위치정보 팔요함
discloud = []
# 진행과정
# 구름에 이동을 M번 명령
for go in info:
    # 1. 모든 구름 di 방향 s만큼 이동
    # 2. 각 구름에서 비, 칸의 바구니 물의 양 1 증가
    move(go[0], go[1], cloud, N)
    # 3. 구름 모두 사라짐
    cloud = []
    # 구름 다 이동시키면
    # 4. 물이 증가한 칸, 물복사버그 마법
    water_copy_bug(discloud)
    # 5. 저장된 물의 양 2 이상인 모든 칸에 구름 생김, 물의 양 2 줄어든다.
    # 3 에서 사라진 구름의 위치이면 안된다
    for i in range(N):
        for j in range(N):
            if (i, j) not in discloud and A[i][j] >= 2:
                cloud.append((i, j))
                A[i][j] -= 2
    # 사라진 구름들의 위치도 다음 이동에서 새로 사용하므로 초기화
    discloud = []

# M번의 이동이 끝난 후 물의 양의 합
total = 0
for row in A:
    total += sum(row)

print(total)
