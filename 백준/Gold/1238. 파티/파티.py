'''파티
- 마을 : N 개의 숫자로 구분 (1 <= X <= N)
    - 각각의 마을에 한 명의 학생 삶

- 파티 : X 번 마을

- 도로 : M개
    - 단반향
    - i 번째 길을 지나는데 Ti 의 시간 소비

- 최단시간으로 파티에 왔다 가기를 원함
- 오고 가는데 가장 많이 시간을 소비하는 학생?

- 최단 시간 문제이므로 다익스트라 사용
- 각 학생이 X 번 집으로 가는 최단 시간
    - 모든 학생들에 대해 X 까지 가는 최단 거리 조사
    - 근데 만약 다른 집에서 출반 한 경우에 거친 집들은 알아서 최단 시간 구해지고
    - 이렇게 구해진 집은 따로 구하러 안가도 된다
- 각 학생이 X 번 집에서 각자의 집으로 가는 최단 시간
    - X 번집에서 출발하여 모든 집을 거칠 때 까지 탐색하면
    각자의 집까지 가는 시간의 최단 시간이 나옴

- 앞애서 오고 가는 걸 각각 구해줘야 하므로
dis_go = [0]*(N+1)  : 각각의 마을에서 X 번 까지 가는데 걸리는 최단 시간
dis_come = [0]*(N+1) : X 번 집에서 각각의 집까지 가는데 걸리는 최단 시간
total = [0] * (N+1) : 각각의 마을에서 오고가는데 걸린 시간'

- 좀 더 생각해볼거
    - X번에서 모든 마을까지의 최단 시간을 한번에 구할 수 있는 거 처럼
    - 모든 마을에서 X 번 까지의 최단 시간을 한번에 구할 수 있다.

    - 좀만 더 생각해보면 결국 모든 경로는 X를 가기 위해 존재하는데
    - 일반적으로 이를 그대로 구현하면 X 를 제외한 모든 곳에서 다익스트라를 이용하여
    - 최단 거리를 구하려 한다.
    - 하지만 만약 단방향의 방향을 뒤집으면
    - 모든 마을에서 X 까지의 최단 시간 = 뒤집어진 도로를 통한 X에서 마을까지의 최단 시간
    - 좀 더 생각해보면 훨씬 효율적인 코드를 만들 수 있다.
'''
import sys, heapq
input = sys.stdin.readline

# X에서 다른 집들로
def dijk(start, go):
    global total

    INF = int(1e9)
    distance = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dis, now = heapq.heappop(pq)

        # 이미 방문 + 이미 최소값 존재하면
        if distance[now] < dis:
            continue

        # 각 지역의 최소값 더해주기
        total[now] += dis

        # 인접 지역 탐색
        for next in go[now]:
            # 이미 방문했으면 패스
            next_node = next[0]
            dis_to_next = next[1]
            # 새로운 누적 시간 계산
            new_dis = dis + dis_to_next
            # 만약 새로 계산된 누적 값이 기존에 있는 거보다 크거나 같으면
            # 해당 지역 재탐색 하지 말자
            if distance[next_node] <= new_dis:
                continue
            # 작은 값 들어오면 갱신해주고
            distance[next_node] = new_dis
            # 다음 탐색지역에 우선순위 매개변수인 누적합과 함께 추가
            heapq.heappush(pq, (new_dis, next_node))


N, M, X = map(int, input().split())
# 도로정보 리스트
road = [[] for _ in range(N+1)]
reverse_road = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int, input().split())
    # 각각의 도로의 시작점에 도착지와, 걸리는 시간 저장
    road[s].append((e,t))
    reverse_road[e].append((s,t))

total = [0] * (N+1)

# X에서 각각의 집까지 가는데 최소시간
dijk(X,road)
# 각각의 집에서 X 까지의 최소시간
dijk(X,reverse_road)

print(max(total))
