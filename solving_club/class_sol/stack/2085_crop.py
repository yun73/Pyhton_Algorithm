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

