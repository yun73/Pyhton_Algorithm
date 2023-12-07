'''
빙산이 두 덩어리 이상으로 분리되는 최초 시간 구하기

두 덩어리 이상으로 분리되지 않으면 프로그램은 0 출력
'''
import sys
input = sys.stdin.readline

def melt():
    global iceberg

    # 빙산 정보 가지고 돌면서 녹이기
    for lo in iceberg.keys():
        if iceberg[lo] == 0: # 녹은 빙산은 건너뛰기
            continue
        x,y = lo
        cnt = 0 # 주변 물의 개수
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and not sea[nx][ny]:
                cnt += 1
        # 녹이기
        iceberg[lo] -= cnt
        # 만약 녹았는데 0 이하가 되면
        if iceberg[lo] <= 0:
            iceberg[lo] = 0

def melt_iceberg():
    global iceberg
    new_iceberg = dict()

    for lo,size in iceberg.items():
        sea[lo[0]][lo[1]] = size
        if size != 0:
            new_iceberg.setdefault(lo,size)
    # 현재 존재하는 빙산 개수 넘겨주기
    return new_iceberg

def is_check():
    global iceberg

    visited = [[0]*M for _ in range(N)]

    for lo in iceberg.keys():
        x,y = lo
        if not iceberg[lo]:
            continue
        if visited[x][y]:
            continue
        visited[x][y] = 1
        q = []
        q.append((x,y))
        cnt = 1 # 이어진 빙산의 개수
        while q:
            i,j = q.pop(0)
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and sea[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                    cnt += 1
        # print(cnt,cnt_iceberg)
        if cnt < len(iceberg):
            return 1
    else:
        return 0


N,M = map(int,input().split())

sea = [list(map(int,input().split())) for _ in range(N)]
iceberg = dict()
# 빙산 정보 저장
for r in range(N):
    for c in range(M):
        # 바다면 건너뛰기
        if sea[r][c] == 0:
            continue
        iceberg.setdefault((r,c),sea[r][c])


# 두 덩어리로 됐는지 체크하는 변수
check = 0
year = 0
while not check:
    # 빙산 녹이기
    melt()
    # 녹인 빙산 정리
    iceberg = melt_iceberg()

    # for line in sea:
    #     print(*line)

    year += 1

    # 분리됐는지 확인
    if is_check():
        check = 1
        break

    if len(iceberg) == 0:
        break

if check:
    print(year)
else:
    print(0)