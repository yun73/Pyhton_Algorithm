import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M, V = map(int, input().split())

near = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    near[n1].append(n2)
    near[n2].append(n1)

for line in near:
    line.sort()

visited = [0]*(N+1)
visited[V] = 1
def dfs(now):
    global stack
    global visited

    print(now, end=' ')
    for next in near[now]:
        if visited[next]:
            continue
        visited[next] = 1
        dfs(next)

dfs(V)
print()
def bfs(start):

    visited = [0]*(N+1)
    q = [start]
    visited[start] = 1
    while q:
        now = q.pop(0)
        print(now,end=' ')
        for next in near[now]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append(next)


bfs(V)