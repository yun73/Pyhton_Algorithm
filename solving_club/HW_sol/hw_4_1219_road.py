T = 10

# 시작점 0 고정, 끝잠 99 고정
# s :  시작 정점
def dfs(s):
    # 방문배열 만들기
    visited = [0] * 100
    # 스ㅡ택
    stack = []
    # 시작정점 방문처리
    visited[s] = 0
    # 현재 정점 번호 i라고 해보자
    i = s

    # 모든 정점 방문할 때까지 반복
    while True:
        # 현재 정점 i가 도착지점인지 확인
        if i == 99:
            return 1

        # 현재 위치에서 방문할 수 있는 j 정점을 확인하고
        # 방문가능하면 방문
        for j in range(100):
            if adj[i][j] == 1 and not visited[j]:
                # j 방문처리
                visited[j] =1
                # 돌아올 위치 기억
                stack.append(i)
                # 다음위치로 이동
                i = j
                # 이전 위치로의 탐색을 중단
                break
        else:
            # 현재위치i에서 방문할 수 있는 j 없었다
            if stack:
                i = stack.pop() # 제일 최근에 방문한 정점으로 돌아가기

            else:
                # 스택이 비어있다 => 갈 수 있는 정점은 모두 방문했다.
                break
    # 반복 끝나고 역까지 오면서 현재 위치가 99가 된적이 없다면
    # 반복 끄난거니까 내가 갈 수 있는 정점 모두 간 상태
    # 길이 없다
    return 0


for tc in range(1,T+1):
    # E : 간선의 개수
    _, E = map(int,input().split())

    # 순서쌍을 배열로 받기
    edges = list(map(int, input().split()))
    # 인접행렬
    adj = [[0] * 100 for _ in range(100)]
    # adj[i][j] ==> i정점에서 j 정점으로 가는 길이 존재

    # 순서쌍을 통해 인접행렬 만들기
    for i in range(E):
        adj[edges[2*i]][edges[2*i+1]] = 1

    print(f'#{tc} {dfs(0)}')
