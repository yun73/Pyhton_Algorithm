# 가장 먼 노드
def bfs(s, V, adj_l, max_time):  # 시작정점 s, 마지막 정점 V
    # 방문체크 리스트 생성
    visited = [0] * (V + 1)
    # 큐 생성
    que = []
    # 시작점 enque
    que.append(s)
    # 현재 정점 방문했다고 추가
    visited[s] = 1

    while que:  # 큐에 정점 남아 있으면
        node = que.pop(0)  # deque로 탐색할 현재 노드 반환
        for e_node in adj_l[node]:  # 현재 노드에 연결되어 있는 노드들 확인
            if visited[e_node] == 0:  # 현재 노드를 아직 탐색하지 않았다면
                que.append(e_node)  # 큐에 추가
                # 해당 노드 방문했다고 표시
                # 근데 이제 지금까지 몇가지 노드 거쳐서 왔는지를 합쳐서
                visited[e_node] = visited[node] + 1
                # 완성된 visited 리스트 안에는 각각의 노드까지 가는데 소요되는 거리가
                # 저장되어 있을 것임
                if max_time < visited[e_node]:
                    max_time = visited[e_node]

    return visited, max_time


def solution(n, edge):
    # 간선정보 인접 리스트로 수정
    # 인접 리스트 생성 (사용하지 않는 인덱스 0 존재)
    adj_l = [[] for _ in range(n+1)]
    for e in edge:
        adj_l[e[0]].append(e[1])
        adj_l[e[1]].append(e[0])  # 방향 조건 없는 경우


    # 방문 기록에서 최대 값
    max_time = 0
    visited, max_time =bfs(1, n, adj_l, max_time)
    # 가장 멀리 떨어진 노드의 개수 구하기
    answer = 0
    for i in range(1,n+1):
        if visited[i] == max_time:
            answer += 1

    return answer

