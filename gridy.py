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
- BFS의 시간복잡도는 O(V+E)인 반면에 다익스트라는 O((V+E)logV)
- 이문제는 BFS 로 해결하여야 함
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
visited = [-1] * 100001

def bfs(start, end):
    global cnt
    q = deque([start])
    visited[start] = 0
    while q:
        now = q.popleft()
        if now == end:
            return
        # 다음 위치 탐색
        for i, next in enumerate((now + 1, now - 1, now * 2)):
            # print(i,next)
            # 더해주는 시간
            res = 1
            if i == 2:
                res = 0
            if 0 <= next <= 100000:
                if visited[next] == -1:
                    visited[next] = visited[now] + res
                    if i == 2:
                        q.appendleft(next)
                    else:
                        q.append(next)

                elif visited[next] >= visited[now] + res:
                    visited[next] = visited[now] + res
                    if i == 2:
                        q.appendleft(next)
                    else:
                        q.append(next)


if N == K:
    print(0)
else:
    bfs(N,K)
    print(visited[K])


