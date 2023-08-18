# 노드의 거리 구하기

def bfs(S, V, G):
    # 방문 리스트 생성
    visited = [0] * (V + 1)
    # 큐생성
    que = []
    # 현재 위치 인큐
    que.append(S)
    # 현재 위치 방문 표시
    visited[S] = 1

    while que:  # 큐가 다 비면 다 탐색한거임
        if visited[G] > 0:  # 도착지 도달하면
            return visited[G] - 1  # 도착지까지 최소 간선 개수 반환

        # 현재 탐색할 위치 반환
        now = que.pop(0)  # deque
        # 현재 위치에서 갈 수 있는 곳 찾기
        for next in adj_l[now]:
            # 방문하지 않은 곳이면
            if visited[next] == 0:
                # que 에 탐색할 곳으로 추가
                que.append(next)
                # 방문기록 남기고 거기까지 가는데 든 거친 노드수 추가
                visited[next] = visited[now] + 1

    # 다 돌았는데도 도착점을 못찾으면
    return 0


T = int(input())
for tc in range(1, T + 1):
    # V : 노드의 개수, C : 간선의 개수
    V, C = map(int, input().split())
    # 간선정보 인접 리스트 => 노드 번호를 인덱스로 쓸거라 크기 +1
    adj_l = [[] for _ in range(V + 1)]
    # 간선 정보 C 만큼 반복하여 입력받기
    for _ in range(C):
        s, e = map(int, input().split())
        adj_l[s].append(e)
        adj_l[e].append(s)  # 방향성 없으므로 반대방향도

    # 출발노드 S, 도착노드 G
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, V, G)}')
