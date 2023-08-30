# N*N 숫자카 적힌 칸
# 오른쪽이나 아래로만 이동 가능
# 맨왼쪽 위에로 오른쪽 아래까지
# 지나는 칸에 써진 숫자의 합 최소 되도록
def is_valid(r, c, N):
    if 0 <= r < N and 0 <= c < N:
        return True
    else:
        return False


def go(r, c, N, nowsum):
    global min_sum

    # 종료 조건 : 맨 오른쪽 끝에 도착
    if r == N - 1 and c == N - 1:
        # 만약 지금까지 합해진 값이 최소값보다 작으면
        if min_sum > nowsum:
            # 갱신해줘
            min_sum = nowsum
        return
    # 해당 위치에서 갈수있는 곳으로 가기
    else:
        # 오른쪽 좌표
        rr, rc = r, c + 1
        # 아래쪽 좌표
        ur, uc = r + 1, c
        # 오른쪽 왼쪽 각각 갈 수 있으면 가봐
        if is_valid(rr, rc, N):
            go(rr, rc, N, nowsum + arr[rr][rc])

        if is_valid(ur, uc, N):
            go(ur, uc, N,   nowsum + arr[ur][uc])

T = int(input())
for tc in range(1, T + 1):
    # 칸수
    N = int(input())
    # 숫자들
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 경로의 최소합
    min_sum = N*N*10+1
    # 경로별 합 구하러 고
    go(0, 0, N, arr[0][0])

    print(f'#{tc} {min_sum}')
