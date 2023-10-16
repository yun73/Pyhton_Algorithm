'''
숨바꼭질

- 수빈이 위치 : N (0~100,000)
- 동생 위치 : K (0~100,000)

- 수빈
    - 걷기 : X - 1 or X + 1
    - 순간이동 : 2*X

- 현재 위치에서 가능한 이동은 총 3가지
- 각 위치에서 3가지 이동을 반복하며 동생을 찾을 때까지 반복
- BFS 탐색
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
visited = [-1] * 100001

def bfs(start, end):
    q = deque([start])
    visited[start] = 0

    while q:
        now = q.popleft()
        if now == end:
            return visited[end]
        # 다음 위치 탐색
        for next in (now + 1, now - 1, now * 2):
            if 0 <= next <= 100000 and visited[next] == -1:
                visited[next] = visited[now] + 1
                q.append(next)

print(bfs(N,K))


