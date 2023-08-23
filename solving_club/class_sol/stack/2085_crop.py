'''
1
5
14054
44250
02032
51204
52212
'''
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    crop = [list(map(int,input())) for _ in range(N)]

    all = 0
    k = 0
    i = N // 2
    r = 0
    while k <= N // 2:
        for c in range(i-k,i+k+1):
            all += crop[r][c]
            all += crop[N-r-1][c]
        r += 1
        k += 1

    for du in crop[N // 2]:
        all -= du

    print(f'#{tc} {all}')

# 인덱스 사용안하고 풀기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 농작물 정보
    field = [list(map(int, input())) for _ in range(N)]

    # 수확한 농작물
    crops = 0

    # 밭의 정 중앙 과의 거리가 d 이하인 곳만 수확
    d = N // 2
    # 밭의 중앙 좌표
    center = (d, d)

    for r in range(N):
        for c in range(N):
            # 거리 계산 방법
            # abs|r - d| + abs|c - d| <= d 이면 농작물 수확
            if abs(r - d) + abs(c - d) <= d:
                crops += field[r][c]

    print(f"#{tc} {crops}")