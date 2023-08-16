

def f(r,N,subsum):
    global min_sum
    # 합치다가 min_sum 보다 커지면 그냥 다음단계로 가자
    if subsum > min_sum:
        return
    # 종료 조건
    if r == N:
        if min_sum > subsum:
            min_sum = subsum
        return
    else:
        for c in range(N):
            if bit[c] == 0:
                bit[c] = 1
                f(r+1, N, subsum+arr[r][c])
                bit[c] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 배열크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    bit = [0] * N
    min_sum = 100

    f(0,N,0)
    print(f'#{tc} {min_sum}')


