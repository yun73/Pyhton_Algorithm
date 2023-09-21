# 최소 시간

# 출발 항상 0,0 에서 도착 N-1,N-1
# 상하좌우 인접지역으로만 이동 가능

# 복구 비용은 인접 칸의 깊이 만큼

import heapq

def dijkstra():
    # 우선순위 큐 생성
    pq = []

    # 출발 지점초기화
    heapq.heappush(pq, (0, 0, 0))
    acc_time[0][0] = 0

    while pq:
        # 현재 시점 가장 누적시간 짧은 노드 정보
        now, r, c = heapq.heappop(pq)

        # 이미 방문한 지점인데 저장된 누적시간이 더 짧으면 여기는 안봐도 돼
        if acc_time[r][c] < now:
            continue

        # 인접지역 상하좌우 탐색
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:

                # 다음 노드로 가기 위한 누적 사용
                # 깊이 만큼 복구 시간
                new_time = now + depths[nr][nc]

                # 누적거리가 다음 위치의 기존 누적 시간보다 크면 안봐도 돼
                if acc_time[nr][nc] <= new_time:
                    continue

                acc_time[nr][nc] = new_time
                heapq.heappush(pq, (new_time, nr, nc))

    return acc_time[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    # 지역 크기
    N = int(input())

    # 깊 정보
    depths = [list(map(int, input())) for _ in range(N)]

    INF = int(1e9)
    # 누적 시간
    acc_time = [[INF] * N for _ in range(N)]

    print(f'#{tc} {dijkstra()}')
