# 메모이스트 써서 다시 해보자
# 최소일 때 작은 번호도 갱신해주는 거 까지
# 연속한 1의 개수 문제로 바꾸자를
didj = [[0,1], [1,0], [0,-1], [-1,0]]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ones = [0] * (N*N+1) # 연속으로 1이 커지는 경우를 표시할 배열
    for i in range(N):
        for j in range(N):
            for di,dj in didj:
                ni, nj = i+di, j+ dj # arr[i],[j]의 주변칸이
                if 0<=ni<N and 0<= nj<N and arr[i][j] + 1 == arr[ni][nj]:
                    ones[arr[i][j]] = 1
    max_cnt = 0
    max_start = 0
    c = 0
    for k in range(N*N, 0 , -1):
        if ones[k]:
            c += 1
            if max_cnt<c:
                max_cnt = c
                max_start = k
            elif max_cnt == c:
                max_start = k
            else: # cnt[k] 가 0이면
                c = 0

    print(f'#{tc} {max_start} {max_cnt+1}')