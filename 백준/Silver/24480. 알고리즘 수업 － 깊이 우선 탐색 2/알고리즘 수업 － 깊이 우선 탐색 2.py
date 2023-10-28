'''
알고리즘 수업 - 깊이 우선 탐색 1

- DFS
- N 개의 정점 : 1 ~ N
- M개의 간선 : 모든 간선 가중치 1
- 무방향 그래프
- 정점 R 에서 시작하여 깊이 우선 탐색으로 노드 방문
- 방문 순서 출력


'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, R):  # V : 방문 순서, graph: 간선 집합, R : 시작 정점
    global visited
    global order

     # 시작 정점 R을 방문 했다고 표시한다.
    for x in graph[R]: # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        # 현재 위치가 갈 수 있는 곳이고 아직 방문을 안했으면
        if not visited[x]:
            # 순서 1증가
            order += 1
            visited[x] = order
            # 해당 정점으로 가보자
            dfs(graph, x)



N, M, R = map(int, input().split())
# 오름 차순으로 방묺해야 하니까 인접 노드 그래프를 행렬로 하는게 더 좋음
# 근데 메모리를 너무 많이 잡아 먹는 거 같으니 인접 리스트로 해보자
# graph = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1) # 정점 i 의 방문 순서 저장
order = 1
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,N+1):
    graph[i].sort(reverse=True)

visited[R] = 1
dfs(graph,R)

for i in range(1,N+1):
    print(visited[i])

