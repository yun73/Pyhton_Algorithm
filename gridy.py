# 최단 경로
import sys
import heapq
input = sys.stdin.readline
def dijkstra(start):
    global dist

    # 우선순위 큐 생성
    pq = []
    # 출발점 초기화
    dist[K] = 0
    heapq.heappush(pq, (0,start))

    while pq:
        w, now = heapq.heappop(pq)

        # 이미 방문한 지점, 누적가중치가 더 작게 방문한 적 있으면
        if dist[now] < w:
            continue

        # 인접 노드들 검색
        for next in near[now]:
            w_to_next = next[0]
            next_node = next[1]

            # 새로운 누적 가중치를 계산하자
            new_w = dist[now] + w_to_next

            # 만약 다음 노드에 저장된 누적 가중치보다 크거나 같으면 그냥 넘어가
            if dist[next_node] <= new_w:
                continue
            # 만약 더 작은값 오면
            # 갱신해주고
            dist[next_node] = new_w
            # 힙에 넣어줘
            heapq.heappush(pq, (new_w,next_node))

# 정점 개수 V, 간선 개수 E
V, E = map(int, input().split())
# 시작 정점의 번호
K = int(input())
# 인접 리스트
near = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    near[s].append((w,e))

INF = int(1e20)
# 누적 가중치 리스트
dist = [INF]*(V+1)

dijkstra(K)

for i in range(1,V+1):
    if dist[i] == INF:
        print('INF')
        continue

    print(dist[i])

