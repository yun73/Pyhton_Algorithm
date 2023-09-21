'''
인수의 생일 파티

- 마을
    - N 개의 집 : 한명씩
    - 각 집을 정점으로 보자
- 도로
    - 집 -> 다른집  가는 단방향 간선
    - 각 도로마다 이동시간 정해짐 = 가중치!
- 인수의 집 : X 번 집
    - 1~ N 번의 집 중

- 상황
    - 모든 마을 사람들이 인수의 생일을 축하해주기 위해
    - 자기집 -> X(인수의 집) -> 자기집
    - 이동하는데 걸리는 시간 최단 시간으로
    -> 경로 겹치는 구간을 누적합 이용?

- 구해야 되는거
    - X 번 집으로 오고 가는데 가장 올래 걸리는 집의 시간

-
# X 번 집에서 다른 집들 까지의 최소 시간
# 각각의 집에서 X 번 까지 갈 때의 최소 시간

'''
import heapq
# x 까지 가는거
def dijk1(start):
    INF = int(1e9)
    distance = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dis, now = heapq.heappop(pq)
        if now == X:
            return dis
        # 이미 방문 + 이미 최소값 존재하면
        if distance[now] < dis:
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
            if distance[next_node] <= new_dis:
                continue
            # 작은 값 들어오면 갱신해주고
            distance[next_node] = new_dis
            # 다음 탐색지역에 우선순위 매개변수인 누적합과 함께 추가
            heapq.heappush(pq, (new_dis, next_node))


def dijk2(start):
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
        for next in road[now]:
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

    return distance

T = int(input())
for tc in range(1,T+1):
    # N : 집의 개수, M : 도로의 개수, X : 인수의 집 번호
    N,M,X = map(int,input().split())

    road = [[] for _ in range(N+1)]
    for _ in range(M):
        # x : 출발집 ,y : 도착집 , c : 걸리는 시간
        x,y,c = map(int, input().split())
        # 도착 집과 걸리는 시간을 저장
        road[x].append((y,c))

    total = [0] * (N + 1)

    # 각각의 집에서 X 까지의 최소시간
    for start in range(1,N+1):
        if start == X:
            dijk2(start)
            continue
        total[start] += dijk1(start)

    print(f'#{tc} {max(total)}')

