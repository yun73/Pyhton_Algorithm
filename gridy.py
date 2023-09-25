'''
특정한 최단 경로

- 무방향 그래프
- 상황
    - 세준이는 1번 정점  N번 정점으로 최단거리 이동 => 그래프 + 최단거리 = 다익스트라

- 조건
    - 임의로 주어진 두 정점은 반드시 통과해야 한다.
    - 한 번 이동했던 정점, 한번 이동했던 간선도 다시 이동할 수 있음
    - 하지만 반드시 최단경로로

- 주어진 두 정점을 반드시 거치면서 최단경로로 이동할 때 최단 경로의 길이를 구해라

- 1번에서 v1,v2 / v1 에서  v2 /v1,v2에서 N번까지 중에 최소값들끼리 더하면??

2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000
'''
import sys
import heapq
input = sys.stdin.readline

def dijk(s,e):
    INF = int(1e10)
    distance = [INF] * (N + 1)

    # 우선순위 큐 생성
    pq = []

    # 초기화
    distance[s] = 0
    # 출발점 넣기
    heapq.heappush(pq, (0,s))

    while pq:
        acc_dis, now = heapq.heappop(pq)

        # 만약 가져온 누적 거리가 현재 저장된 누적거리보다 크면 pass
        if distance[now] < acc_dis:
            continue

        # 인접노드들을 순회하며
        for next in range(1,N+1):
            # 갈 수 없으면 지나쳐
            if not graph[now][next]:
                continue
            # 갈수 있으면
            # 새로운 누적값 계산
            new_acc = acc_dis + graph[now][next]
            # 만약 새로운 누적값이 이미 존재하는 거보다 크면 지나쳐
            if distance[next] < new_acc:
                continue
            # 아니면 갱신해주고 우선순위에 넣어줘
            distance[next] = new_acc
            heapq.heappush(pq, (new_acc, next))

    return distance


# N : 정점 개수, E : 간선개수
N, E = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

# 간선 E 개의정보
for _ in range(E):
    # s 번정점에서 e 번 정점까지 d 거리만큼 양방향 길
    s, e, d = map(int, input().split())
    graph[s][e] = d
    graph[e][s] = d

INF = int(1e10)
# 반드시 거쳐야 할 두 정점
v1, v2 = map(int, input().split())

result = 0
# 만약 전체 돌았는데 안나오면 -1 출력
one_to_N = dijk(1,N)
if one_to_N[v1] == INF or one_to_N[v2] == INF or one_to_N[N] == INF:
    result = -1
else:
    # v1 > v2 = v2 > v1
    v1_v2 = dijk(v1, v2)
    result += v1_v2[v2]

    # 두가지 경우

    # 1 > v2 > v1 > N
    res1 = 0
    # 1번에서 v1
    one_to_v1 = dijk(1,v1)
    res1 += one_to_v1[v1]
    # v2에서 N
    v2_to_N = dijk(v2,N)
    res1 += v2_to_N[N]

    # 1 > v2 > v1 > N
    res2 = 0

    # 1번에서 v2
    one_to_v2 = dijk(1, v2)
    res2 += one_to_v2[v2]
    # v1에서 N
    v1_to_N = dijk(v1, N)
    res2 += v1_to_N[N]

    result += min(res1,res2)

print(result)

# print(dijk(v1,v2))
# print(dijk(1,N))
# print(dijk(1,v1))
# print(dijk(1,v2))
# print(dijk(N,v1))
# print(dijk(N,v2))
'''
[10000000000, 3, 0, 3, 5]
[10000000000, 0, 3, 5, 4]
[10000000000, 0, 3, 5, 4]
[10000000000, 0, 3, 5, 4]
[10000000000, 4, 4, 1, 0]
[10000000000, 4, 5, 1, 0]
'''
