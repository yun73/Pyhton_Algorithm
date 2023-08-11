T = int(input())
# 우 아 왼 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T+1):
    N, M = map(int,input().split())
    site = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0

    for r in range(N):
        for c in range(M):
            if site[r][c] == 1:
                for d in range(4):
                    length = 1
                    nr = r + dr[d]
                    nc = c + dc[d]
                    while True:
                        if 0<=nr<N and 0<=nc<M and site[nr][nc] == 1:
                            length += 1
                            nr += dr[d]
                            nc += dc[d]
                        else:
                            break
                    if max_len <= length:
                        max_len = length

    print(f'#{tc} {max_len}')