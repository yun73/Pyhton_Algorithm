# 최소비용

# 출발 항상 0,0 에서 도착 N-1,N-1
# 상하좌우 인접지역으로만 이동 가능

# 기본 연료 1, 높이 차이만큼 추가 연료

import heapq

def dijkstra():
    
    # 우선순위 큐 생성
    pq = []

    # 출발 지점초기화
    heapq.heappush(pq, (0, 0, 0))
    acc_use[0][0] = 0



    while pq:
        # 현재 시점 가장 누적거리 짧은 노드 정보
        nowuse, r, c = heapq.heappop(pq)

        # 이미 방문한 지점인데 저장된 누적거리가 더 짧으면 여기는 안봐도 돼
        # 음의 가중치가 있을 때 이부분을 없애면 일단 저장 안된부분은 감
        #  
        if acc_use[r][c] <= nowuse:
            continue

        # 인접지역 상하좌우 탐색
        for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr ,nc = r+dr, c +dc
            if 0<=nr<N and 0<=nc <N:

                # 다음 노드로 가기 위한 누적 사용
                # 기본 소비 1에 높이 차이값만큼 누적
                # 만약 내리막에서 높이차만큼 연료를 절약한다는 조건이 있으면??
                # 벨만포드로 해결 or 다익스트라에서 방문한데도 다시 방문??
                new_use = nowuse + 1
                sub = heights[nr][nc]-heights[r][c]
                if sub > 0:
                    new_use += sub

                # 누적거리가 다음 위치의 기존 누적 거리보다 크면 안봐도 돼
                if acc_use[nr][nc] <= new_use:
                    continue

                acc_use[nr][nc] = new_use
                heapq.heappush(pq,(new_use,nr,nc))

    return acc_use[N-1][N-1]

T = int(input())
for tc in range(1,T+1):

    # 지역 크기
    N = int(input())
    
    # 높이 정보
    heights = [list(map(int, input().split())) for _ in range(N)]

    INF = int(1e9)
    # 누적 연료 소비량
    acc_use = [[INF] * N for _ in range(N)]

    print(f'#{tc} {dijkstra()}')
