# 동철이의 일 분배
# 직원들에게 공평하게 일을 하나씩 배분

def bt(i,N,p): # i번째 사람, 총 N 명, 확률
    global max_P

    if i == N:
        if max_P < p:
            max_P = p
        return
    # 곱해지는 최대값이 1인데
    # 최대 확률보다 작은게 나와버리면 앞으로도 작을 것이다
    if p <= max_P:
        return

    # 재귀호출
    for j in range(N):
        if not clear[j]:
            clear[j] = 1
            bt(i+1,N,p*(P[i][j]/100))
            clear[j] =0


T = int(input())
for tc in range(1,T+1):
    # 직원 수, 해야할 일
    N = int(input())
    # i 번 직원이 j 번 일을 하면 성공할 확률이 Pi,j
    # 주어진 일이 모두 성공할 확률의 최대값을 구해
    P = [list(map(int, input().split())) for _ in range(N)]

    # j 번 일을 누군가 했는지에 대한 리스트
    clear = [False] * N
    # 모두 성공할 확률의 최대값
    max_P = 0

    bt(0,N,1)

    print(f'#{tc} {max_P*100:.6f}')