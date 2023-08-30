# 사무실 -> 관리구역 전부 -> 사무실
# 각 구역 한 번씩만 방문 -> 최소배터리 사용량
# 1번 사무실 2번 ~ N번 관리구역 번호
# N번 줄 도착하면 다시 1로 가야함

def go(move, r, c, nowuse):
    global min_use
    global visit

    # 종료 조건 : 이동을 N 번 하면 1-2-3-1 마지막은 무조건 1로 가야함
    if move == N-1:
        nr,nc = c,0
        nowuse += site[nr][nc]
        if min_use > nowuse:
            min_use = nowuse
    else:
        # 다음 위치 탐색
        for i in range(1,N):
            # 아직 방문한 적 없는데 면
            if visit[i] == 0:
                # 다음 위치를 갱신해주고
                nr,nc = c, i
                # 방문했다고 표시하고
                visit[i] = 1
                # 그 다음 지역 가봐
                go(move+1,nr,nc,nowuse + site[nr][nc])
                # 갔다오면 방문안했다고
                visit[i] = 0
                # 하고 다른 경우로 for문


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 사무실과 지역 정보
    site = [list(map(int, input().split())) for _ in range(N)]
    # site[r][c] : 현재위치 r, 다음위치 c

    # 최소 소비량
    min_use = 100*11
    # 초기 r은 무조건 0
    # 마지막 c는 무조건 0
    r,c = 0,0
    # 방문한 지역 체크
    visit = [0]*N
    go(0,r,c,0)
    print(f'#{tc} {min_use}')