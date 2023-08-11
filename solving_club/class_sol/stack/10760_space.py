dr = [0,1,1,1,0,-1,-1,-1]
dc = [1,1,0,-1,-1,-1, 0, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    aij = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 주변 8개 지역 격자 돌려서
    for i in range(N):
        for j in range(M):
            cnt = 0
            for d in range(8):
                ni = i + dr[d]
                nj = j + dc[d]
                if 0 <= ni < N and 0 <= nj < M and aij[ni][nj] < aij[i][j]:
                    cnt += 1

            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')