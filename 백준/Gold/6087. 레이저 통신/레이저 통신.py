'''
레이저 통신

- 지도 : W x H 크기
    - '.' : 빈칸
    - '*' : 벽
    - 'C' : 레이저

- 거울 : '/', '\' 두종류
    - 근데 모든 방향으로 꺾을 수 있으니까 거울 종류는 영향 없음

-  두 레이저를 거울을 사용하여 연결, 최소 거울 수

- C to C 상황에서 최소 거울수를 찾아야 하므로 bfs, 다익스트라 등 사용 가능

1. 일단 레이저의 위치를 찾자
2. 사용한 거울 수를 기록하면서 가야됨
3. 방문 표시도 해주자 1e9로
4. 이전의 방향 값을 알아야 함

'''
import heapq

# 방향 동서 남북
di = [(0,1),(0,-1),(1,0),(-1,0)]
di_dict = {0:1, 1:0 , 2 :3 , 3 :2}

def is_valid(x,y):
    if 0<=x<H and 0<= y<W:
        return True
    return False

# 방향 확인
def di_check(before,next):
    # 이전거에서 온 방향과 같은 방향이면
    if before == next:
        return 0
    # 90도 돌린 곳이라면
    if before != di_dict[next]:
        # 거울개수 1 추가
        return 1
    # 180 도 돌린 곳은 가면 안됨
    return -1


W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]
visited = [[[int(1e9)]*4 for _ in range(W)] for _ in range(H)]
# for r in visited:
#     print(r)
# 시작점 찾기
C= []
for r in range(H):
    for c in range(W):
        if arr[r][c] == 'C':
            C.append((r,c))

for i in range(4):
    visited[C[0][0]][C[0][1]][i] = 0

def dijk(sr,sc):

    # 우선순위 큐 생성
    pq = []
    # 처음 4방향 넣어주기
    for next_d in range(4):
        nsr, nsc = sr + di[next_d][0], sc + di[next_d][1]
        if is_valid(nsr,nsc) and arr[nsr][nsc] != '*':
            visited[nsr][nsc][next_d] = 0
            heapq.heappush(pq, (0, next_d, nsr, nsc))

    while pq:
        now,before_d, i, j = heapq.heappop(pq)
        if arr[i][j] == 'C' and not (i,j) == (sr,sc):
            return
        # 현재 위치에서 갈 수 있는 방향 탐색
        for next_d in range(4):
            # 이전 방향과 다음에 갈 방향 체크한 후 정보 넘겨주기
            # 이전에 있던 곳은 탐색 안할거야
            result = di_check(before_d, next_d)
            if result == -1:
                continue
            ni,nj = i+di[next_d][0], j+di[next_d][1]
            # 일단 범위내에 있고 벽이 아니라면
            if is_valid(ni,nj) and arr[ni][nj] != '*':
                # 만약 들어있는 값이 더 작으면 추가 하지 말자
                next = now + result
                if visited[ni][nj][next_d] <= next:
                    continue

                visited[ni][nj][next_d] = next
                heapq.heappush(pq,(next,next_d,ni,nj))
        # for r in visited:
        #     print(r)
        # print('++++++++++')

dijk(C[0][0],C[0][1])
print(min(visited[C[1][0]][C[1][1]]))
