di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0  #
    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]  # 터트린 풍선의 꽃가루 수
            for k in range(4):  # i,j 인접에 대해
                ni, nj = i + di[k], j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    cnt += arr[ni][nj]
            if max_v < cnt: # i, j 인점 풍선까지 더하고나면
                max_v = cnt

    print(f'#{tc} {max_v}') # 모든 위치에서 확인이 끝나면
