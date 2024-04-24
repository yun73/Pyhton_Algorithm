from collections import deque
import sys

input = sys.stdin.readline

def bfs(now):
    q = deque([now])
    visited = [0] * (N+1)
    visited[now] = 1
    cnt = 0
    while q:
        next = q.popleft()
        for can in trust[next]:
            if not visited[can]:
                q.append(can)
                visited[can] = 1
                cnt += 1

    return cnt

N, M = map(int, input().split())
trust = [[] for _ in range(N+1)]
# 각 지점을 해킹하면 최대 몇개 해킹 가능한지

for _ in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

res = []
max_cnt = 0
for i in range(1, N+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        res = []
        res.append(i)
    elif cnt == max_cnt:
        res.append(i)

print(*res)