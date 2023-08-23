# 가장 나중에 연락을 받게 되는 가람 중 번호가 가장 큰 사람
# 한명 거쳐갈 때마다 그전 방문기록에 1씩 더하고 해당 칸에 방문해서 수행했을 때
# visited 값이 젤 큰 사람이 가장 나중에 연락을 받는 사람임

def bfs(S):
    # 방문기록 리스트 생성
    visited = [0] * 101
    # 큐 생성
    que = []
    # 현재 위치 인큐
    que.append(S)
    # 방문기록 남기기
    visited[S] = 1
    last_call = 0
    # 주어진 통화 경로 모두 돌 때까지
    # 출발점에서 안이어지는데도 안돎
    while que:
        # 현재위치 반환
        now = que.pop(0) # 디큐
        for next in all[now]:
            if visited[next] == 0:
                que.append(next)
                visited[next] = visited[now] + 1

                # 가장 나중에 연락될 때의 연락값 갱신
                if last_call < visited[next]:
                    last_call = visited[next]

    last_person = 0
    for i in range(101):
        if visited[i] == last_call:
            last_person = i

    return last_person


T = 10
for tc in range(1,T+1):
    E, S = map(int, input().split())
    # 전체 비상 연락망 만들기
    all = [[] for _ in range(101)]
    con = list(map(int, input().split()))
    for i in range(0,E, 2):
        all[con[i]].append(con[i+1]) # 방향성이 있음

    print(f'#{tc} {bfs(S)}')
