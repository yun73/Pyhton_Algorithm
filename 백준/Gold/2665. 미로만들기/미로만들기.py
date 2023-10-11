'''
미로만들기

- 방 : nxn 바둑판 모양 n**2 개의 방
    - 검은방 : 못들어감
    - 흰방 이동 가능

- 시작점 : 0,0 and 도착점 : n-1,n-1
- 시작점에서 도착점까지 못도착하는 경우 최대한 적게 문을 부시면서 가고 싶다

1. 가는 방향은  상하좌우
2. bfs 탐색을 하되 지금까지 부신 검은 벽의 개수를 우선순위로 이용하여 heapq, 우선순위 큐사용
>> 다익스트라
3. 도착점 도달하면 그 즉시 종료
    - 우선순위 높은 즉 문을 가장 적게 부시면서 온 얘
'''

import sys, heapq
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[int(1e9)]*n for _ in range(n)]
pq = []
# 출발점 우선순위 큐에 넣고 시작
heapq.heappush(pq, (0,0,0))
visited[0][0] = 0
while pq:
    # 현재 위치
    # 가장 맨 앞 인자는 지금까지 부신 개수
    now , r, c = heapq.heappop(pq)
    # 도착점이면 지금까지 부신 개수 출력
    if (r,c) == (n-1,n-1):
        print(now)
        break
    # 지금 위치 이미 와보고 우선 순위 더 큰게 올경우
    if visited[r][c] < now:
        continue

    visited[r][c] = now

    # 현재위치에서 갈 수 있는 곳 탐색
    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr,nc = r+dr, c +dc
        if 0<=nr<n and 0<=nc<n:
            # 만약 이미 방문했는데 지금 값보다 작거나 같은거 들어가 있으면 다음 탐색에 넣지마
            # 벽이면
            if not rooms[nr][nc]:
                next = now + 1
                if visited[nr][nc] <= next:
                    continue
                visited[nr][nc] = next
                heapq.heappush(pq,(next,nr,nc))
            # 방이면
            else:
                if visited[nr][nc] <= now:
                    continue
                visited[nr][nc] = now
                # 지금 까지 부신거 그대로 들고 추가
                heapq.heappush(pq,(now,nr,nc))
