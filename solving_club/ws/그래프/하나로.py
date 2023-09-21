# 하나로
# N 개의 섬 연결
# 해저터널 반드시 두 섬을 선분으로 연결
# 환경부담 세율 E, 해저터널 길이 L
# E * L**2
# 환경부담금 최소로 모든 섬 연결
import heapq

def prim(start):
    pq = []
    INF = int(1e20)
    MST = [0] * N
    heapq.heappush(pq,(0,start))

    sum_cost = 0

    while pq:
        # 가장작은 코스트인거 꺼내
        cost, now = heapq.heappop(pq)
        # 이미 방문했으면
        if MST[now]:
            continue
        MST[now] = 1
        sum_cost += cost

        # 지금 위치에서의 인접한 섬에대한 코스트
        for next in range(N):
            # 연결 안된데sk 방문한데면
            if graph[now][next] == 0 or MST[next]:
                continue
            heapq.heappush(pq,(graph[now][next],next))

    return sum_cost


T = int(input())
for tc in range(1,T+1):
    # 섬의 개수
    N = int(input())
    # X 좌표
    X = list(map(int, input().split()))
    # Y 좌표
    Y = list(map(int, input().split()))
    # 환경부담 세울
    E = float(input())

    graph = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2) # 환경 부담금 구하기
            graph[j][i] = graph[i][j]

    result = prim(0)

    print(f'#{tc} {round(result*E)}')