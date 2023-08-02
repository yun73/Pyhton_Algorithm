# NxN 배열 파리개수 나타냄
# MxM 크기의 파리채 가지고 있음
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for _ in range(N)]

    # 파리채 영역 탐색 델타
    # 0,0 부터 n,n 까지
    kill_max = 0
    # MxM 크기의 파리채는 (0,0) 칸 기준으로 0~N-M+1 안에서만 움직일 수 있음
    for r in range(N - M + 1):  # 행
        for c in range(N - M + 1):  # 열
            # 현재 위치 flys[r][c]
            # 파리채 크기까지 반복 (1,1) 에서 (M,M) 부분까지
            # 현재위치 (r,c) 에서 (r+M-1, r+M-1) 까지 다 더하기
            # 다 더한값이 퇴치한 파리
            now_kill_fly = 0
            for i in range(0, M):
                for j in range(0, M):
                    nr = r + i
                    nc = c + j
                    now_kill_fly += flys[nr][nc]

            if kill_max < now_kill_fly:
                kill_max = now_kill_fly

    print(f'#{tc} {kill_max}')