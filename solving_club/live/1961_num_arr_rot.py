# NxN 행렬 주어짐
# 회전 배열
def rotate_arr(N, arr):
    ro_arr = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ro_arr[r][c] = arr[N - c - 1][r]

    return ro_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    de_90 = rotate_arr(N,arr)
    de_180 = rotate_arr(N,de_90)
    de_270 = rotate_arr(N,de_180)
    # 최종 배열
    result = [[''] * 3 for _ in range(N)]

    for i in range(N):
        for j in range(N):
            result[i][0] += str(de_90[i][j])
            result[i][1] += str(de_180[i][j])
            result[i][2] += str(de_270[i][j])

    print(f'#{tc}')
    for n in range(N):
        print(*result[n])
    # 90 도 회전
    # 180 도 회전
    # 270도 회전전

1945
5789
6019
16910


