'''

백도어

챔피언 N 개의 분기점
0 : 유섭이의 챔피언
N-1 : 상대 편 넥서스
1,2,N-2 즁간 거점들

안들키고 넥서스 까지 : 0 >> N-1 까지 연결 확인

입력
    - 각 분기점 지나칠 수 있는지 여부
    - 각 분기점과 다른 분기점 까지의 시간 주어짐

>> 0에서 N-1 까지 갈 수 있는 최소 시간
>> 만약 못가면 -1 출력
>> 다익스트라

N, M :  분기점의 수, 분기점들을 잇는 길의 수 .
(1 ≤ N ≤ 100,000, 1 ≤ M ≤ 300,000)
 a0, a1, ..., aN-1 : 적의 시야에 보이는지 N개의 정수
 0 안보이, 1 보임

 넥서스는 상대의 시야에 보이지만 갈 수 있는 곳임에 주의

 a, b, t : a번째 분기점과 b번째 분기점 사이를 지나는데 t만큼의 시간
 연결은 양방향
 (0 ≤ a, b < N, a ≠ b, 1 ≤ t ≤ 100,000)
'''
import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):

    pq = []
    node_min_time[start] = 0
    heapq.heappush(pq,(0,start))

    while pq:
        now_time, now_node = heapq.heappop(pq)

        # 현재 노드까지 이미 최단 시간으로 왔다면
        if node_min_time[now_node] < now_time:
            # 그냥 넘어가기
            continue

        if now_node == N-1:
            return node_min_time[N-1]

        # 현재 노드에서 연결된 리스트 찾기
        for next_node, time in edge[now_node]:
            # 넥서스가 아닌데 와드가 있으면 못갑
            if next_node != N-1 and ward[next_node]:
                continue

            next_time = now_time + time

            # 만약 다음 지점까지 이미 최단 시간으로 갔다면
            if node_min_time[next_node] <= next_time:
                continue

            # 아직 최단 시간으로 안갔다면 최단 시간 저장후 이동
            node_min_time[next_node] = next_time

            heapq.heappush(pq,(next_time,next_node))


    # 만약 다 돌았는데 못 도착하면 -1 리턴
    if node_min_time[N-1] == INF:
        return -1
    else:
        return node_min_time[N-1]


N,M = map(int, input().split())
ward = list(map(int, input().split()))
edge = [[] for _ in range(N)]  # (b,t) t초 걸려서 b
INF = int(1e12)
node_min_time = [INF for _ in range(N)] # 현재 노드까지 최소 시간 저장
for _ in range(M):
    a, b, t = map(int, input().split())
    edge[a].append((b,t))
    edge[b].append((a,t))

# 0에서 출발하여 넥서스까지 최소 시간 출력
print(dijkstra(0))
