'''
타임머신

- 도시 : N 개

- 버스 : M 개
    - A, B, C
        - A : 시작도시
        - B : 도착도시
        - C : 이동시간
            - 양수, 음수
            - 0은 순간이동을 하는 경우
            - C < 0 : 타임머신으로 시간을 되돌아가는 경우

- 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간
- 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서
- 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력

1. 무한히 오래전으로 가는 경우
    - 다 돌고 자기 자신으로 다시 왔을 때 음수 값이면은 무한히 오래전으로 간다

- 음수 가중치가 포함된 최단거리 구하기 문제 : 벨만포드
- 간선정보가 모두 주어지기 떄문에 모든 간선 정보를 확인해주면
- 최단거리가 알아서 구해짐
    - 현재 간선 > 다른 노드로의 이동거리가 더 짧은 경우, 거리 정보 갱신
- n-1번 반복 이후에도 거리 값이 갱신된다면 음수 순환이 존재

- 내가 헷갈렸던 부분
    - 다익스트라와 다르게 매 반복마다 모든 간선 확인
'''

# N: 노드수, M : 간선수
N, M = map(int,input().split())
# 간선정보
edges = []
INF = int(1e9)
# 최단 시간을 저장할 리스트
dist = [INF]*(N+1)
for _ in range(M):
    A,B,C = map(int,input().split())
    # A>B 로 가는 시간 저장, 방향 존재
    edges.append((A,B,C))

# 벨만 포드 알고리즘
def bf(start):
    # 시작점 0으로 초기화
    dist[start] = 0
    # 정점 수 만큼 반복 :
    for i in range(N):
        for j in range(M):
            now = edges[j][0]
            next = edges[j][1]
            time = edges[j][2]
            # 방문한 곳 중에서 이동거리 더 짧은게 들어오면 갱신
            if dist[now] != INF and dist[next] > dist[now] + time:
                dist[next] = dist[now] + time
                # n번째 에서도 값이 갱신되면 음수순환 존재
                if i == N-1:
                    return True
    return False

cycle = bf(1)

if cycle:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i] == INF:
            print(-1)
            continue
        print(dist[i])








