'''
미로 탈출 명령어

- (x,y) -> (r,c)
- 미로 : n x m
    - '.' : 빈공간
    - 'S' : 출발지점
    - 'E' : 탈출지점
- 탈출 조건
    1. 격자 바깥으로 못나감
    2. (x, y)에서 (r, c)까지 이동거리가 총 k여야 함
        - 이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 됨
    3. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출
        - 정렬 한 번 써서 맨 앞에거로 탈출 하자

- 이동경로 문자열
    - l : 왼쪽
    - r : 오른쪽
    - u : 위
    - d : 아래

- 출력
    - 탈출하기 위한 경로 return
    - 조건대로 미로 못 탈출하면 'impossible' return

- 우선 순위 큐로 이동경로를 자체를 넣기
- 알아서 사전순 먼저 탐색한다

- 최소로 갈 수 있는 만큼 가고 그 이후에는 남은 k 만큼 반복하여 더하기
'''
import heapq
# 상하좌우
di = [(1,0),(0,-1),(0,1),(-1,0)]
ds = ['d','l','r','u']
def solution(n, m, x, y, r, c, k):
    # 우선순위 큐 생성
    pq = []
    # 시작 위치 넣어주기
    # 갔던 곳 다시 방문해도 되니까 따로 누적값 기록 안함
    heapq.heappush(pq,('',x,y))
    while pq:
        # 현재 경로 및 위치 반환
        now,i,j = heapq.heappop(pq)
        # 이동해야 하는 거리가 남은 거리보다 크거나 같지 않으면 패스
        if abs(i-r) + abs(j-c) > k-len(now):
            continue
        # 현재 위치에서 도착점까지의 남을 거리가 홀수 이면 그냥 패스
        if (k-len(now)-(abs(i-r) + abs(j-c)))%2:
            continue

        # 만약 k번 만큼 이동했는데
        if len(now) == k:
            return now

        # 현재 위치에서 이동할 수 있는 곳 탐색
        for d in range(4):
            ni,nj = i + di[d][0], j + di[d][1]
            # 만약 범위를 안넘어 가면
            if 1<= ni <= n and 1<= nj <= m:
                # 이동경로를 추가해주고
                next = now + ds[d]
                if len(next) == k:
                    if (ni,nj) != (r,c):
                        continue
                # 다음 탐색 지점에 추가
                heapq.heappush(pq, (next,ni,nj))

    return 'impossible'

