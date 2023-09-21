# 최소 이동 거리
# 연결지점 0 - N 까지의 번호
# E 개의 일방통행 도로구간
# 0 번 부터 N 번까지 가는데의 최소한의 거리
import heapq

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    near = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        near[s].append((e,w))

    INF = int(1e9)
    # 누적거리 리스트 생성
    distance = [INF] * (N+1)

    # 우선순위 큐 생성
    pq = []

    # 시작지점은 0이다. 초기화 작업
    heapq.heappush(pq, (0,0)) # 0번 위치 누적거리, 0번 노드
    distance[0] = 0

    while pq:
        # 현재 시점 누적합 최소인 곳 뽑아서
        # 해당위치와 인접한 곳 탐색
        dis, now = heapq.heappop(pq)
        if now == N:
            break
        # 근데 방문한적이 있고, 지금 들어온 값보다 이미 작은값으면 넘어가자
        if distance[now] < dis:
            continue
        # 작은값이 들어오면
        # 인접한 지역 탐색
        for next in near[now]:
            next_node = next[0]
            dis_to_next = next[1]
            # 새로운 누적 거리 계산
            new_dis = dis + dis_to_next
            # 만약 새로 계산된 누적 값이 기존에 있는 거보다 크거나 같으면
            # 해당 지역 재탐색 하지 말자
            if distance[next_node] <= new_dis:
                continue
            # 작은 값 들어오면 갱신해주고
            distance[next_node] = new_dis
            # 다음 탐색지역에 우선순위 매개변수인 누적합과 함께 추가
            heapq.heappush(pq, (new_dis, next_node))

    print(f'#{tc} {distance[N]}')