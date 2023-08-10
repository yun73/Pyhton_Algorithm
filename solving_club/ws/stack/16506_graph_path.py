def dfs(S, G, V):
    # 방문한 정점 초기화
    visited = [0] * (V+1)
    stack = []
    # 시작 정점 S
    i = S
    visited[i] = 1 # 현재 정점은 방문한 걸로
    # 경로 찾으면 1, 못찾으면 0 반환

    while True:
        # 현재 정점 i, 처음은 출발점인 S에서 갈 수 있는 정점 j 탐색
        for j in adj_l[i]:
            # 만약 빈 adj 가 아니고 visited[j] 가 0 이면
            if visited[j] == 0:
                # j로 갈 수 있으니까 i를 지나므로 stack에 i 추가
                stack.append(i)
                visited[j] = 1
                i = j # 현재 위치를 j로 변경
                if i == G: # 만약 G에 도달하면
                    return 1  # 가능하다고 답 바꾸고 for문 종료, while 문 종료
                # 이 뒤에는 다음 정점으로 넘어가서 다시 탐색해야 하므로
                break
        else: # 현재 정점에서 갈 수 있는 정점이 없으면
            if stack:
                i = stack.pop() # 전 단계로 돌아가서 탐색 i에 전단께 입력해주기
            else:
                break

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V + 1)]  # 0번 인덱스 사용 안해
    for i in range(E):
        s, e = map(int, input().split()) # 시작정점, 끝 정점
        # 유향 그래프 이므로 받는 입력값에 대해서만 adj_l에 추가
        adj_l[s].append(e)

    S, G = map(int, input().split())

    print(f'#{tc} {dfs(S, G, V)}')


