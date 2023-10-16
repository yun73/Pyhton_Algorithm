'''
숨바꼭질 2

- 수빈이 위치 : N (0~100,000)
- 동생 위치 : K (0~100,000)

- 수빈
    - 걷기 : X - 1 or X + 1
    - 순간이동 : 2*X

- 현재 위치에서 가능한 이동은 총 3가지
- 각 위치에서 3가지 이동을 반복하며 동생을 찾을 때까지 반복
- BFS 탐색
'''
import sys, heapq
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
INF = int(1e9)
visited = [INF] * 100001

def bfs(start, end):
    global cnt
    pq = []
    visited[start] = 0
    heapq.heappush(pq,(0,start))
    while pq:
        now_time, now = heapq.heappop(pq)

        # 다음 위치 탐색
        for next in (now + 1, now - 1, now * 2):
            if 0 <= next <= 100000:
                if visited[next] >= now_time + 1:
                    visited[next] = now_time + 1
                    heapq.heappush(pq,(now_time+1,next))
                # 종료점 찾았는데 저장된 거보다 더 큰 거 들어오면 종료
                if next == end:
                    if now_time + 1 > visited[next]:
                        return
                    cnt += 1

cnt = 0
# 같을 때는 한가지만 존재
if N == K:
    print(0)
    print(1)
else:
    bfs(N,K)
    print(visited[K])
    print(cnt)

