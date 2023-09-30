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
total = [0] * (N+1) : 각각의 마을에서 오고가는데 걸린 시간
'''
import sys, heapq
input = sys.stdin.readline


# X 까지 가는거
def dijk_go(start):
    INF = int(1e9)
    dis_go = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    dis_go[start] = 0
    while pq:
        dis, now = heapq.heappop(pq)
        if now == X:
            return dis
        # 이미 방문 + 이미 최소값 존재하면
        if dis_go[now] < dis:
            continue

        # 인접 지역 탐색
        for next in road[now]:
            # 이미 방문했으면 패스
            next_node = next[0]
            dis_to_next = next[1]
            # 새로운 누적 시간 계산
            new_dis = dis + dis_to_next
            # 만약 새로 계산된 누적 값이 기존에 있는 거보다 크거나 같으면
            # 해당 지역 재탐색 하지 말자
            if dis_go[next_node] <= new_dis:
                continue
            # 작은 값 들어오면 갱신해주고
            dis_go[next_node] = new_dis
            # 다음 탐색지역에 우선순위 매개변수인 누적합과 함께 추가
            heapq.heappush(pq, (new_dis, next_node))

# X에서 다른 집들로
def dijk_X(start):
    global total

    INF = int(1e9)
    dis_come = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    dis_come[start] = 0
    while pq:
        dis, now = heapq.heappop(pq)

        # 이미 방문 + 이미 최소값 존재하면
        if dis_come[now] < dis:
            continue

        # 각 지역의 최소값 더해주기
        total[now] += dis

        # 인접 지역 탐색
        for next in road[now]:
            # 이미 방문했으면 패스
            next_node = next[0]
            dis_to_next = next[1]
            # 새로운 누적 시간 계산
            new_dis = dis + dis_to_next
            # 만약 새로 계산된 누적 값이 기존에 있는 거보다 크거나 같으면
            # 해당 지역 재탐색 하지 말자
            if dis_come[next_node] <= new_dis:
                continue
            # 작은 값 들어오면 갱신해주고
            dis_come[next_node] = new_dis
            # 다음 탐색지역에 우선순위 매개변수인 누적합과 함께 추가
            heapq.heappush(pq, (new_dis, next_node))


N, M, X = map(int, input().split())
# 도로정보 리스트
road = [[] for _ in range(N+1)]
for _ in range(M):
    s,e,t = map(int, input().split())
    # 각각의 도로의 시작점에 도착지와, 걸리는 시간 저장
    road[s].append((e,t))

total = [0] * (N+1)

# 각각의 집에서 X 까지의 최소시간
for start in range(1, N + 1):
    # 만약 X 가 나오면 X에서 다른 집들까지의 최소거리들을 total에 더해줘
    if start == X:
        dijk_X(start)
        continue
    # 각 위치에서 X 까지 가는 최단 시간 구하고 total에 더해주기
    total[start] += dijk_go(start)

print(max(total))
