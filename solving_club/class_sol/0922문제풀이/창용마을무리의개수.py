'''
창용 마을 무리의 개수

- 입력값
마을 사람 : N 명 1~N
관계 수 : M
    - M 개의 줄에 걸쳐 서로를 아는 2 사람 번호 주어짐
    - 인접행렬 사용

- 조건
두 사람이 서로를 알고 있는 관계 o,x
    - 만약 아는 관계거나 몇 사람을 거쳐서 알 수 있는 관계라면
        - 하나의 무리로 봄

무리의 개수를 구해라
'''
T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    # 인접 행렬 생성
    near = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        near[p1][p2] = 1
        near[p2][p1] = 1

    # 서로 아는 경우 체크해줄 리스트
    # 다시 탐색하지 않도록
    visited = [0] * (N+1)
    # 전체 그룹의 개수
    group = 0
    # 1번 사람부터 관계있는 사람들 쭉 만나러 가기
    for i in range(1,N+1):
        # 이미 확인한 그룹이면 넘어가
        if visited[i]:
            continue
        
        q = []
        q.append(i)
        visited[i] = 1
        # - BFS
        while q:
            now = q.pop(0)

            # 현재의 사람과 아는 사람들 탐색 
            for next in range(1,N+1):
                # 연결안되어 있거나 이미 방문했으면 넘어가 
                if near[now][next] == 0 or visited[next]:
                    continue

                # 연결된 사람들 방문했다고 체크하고
                visited[next] = 1
                # 다음 탐색에 넣어줘
                q.append(next)
            
        # 다 탐색했으면 그룹 한개 끝난거
        group += 1

    
    print(f'#{tc} {group}')