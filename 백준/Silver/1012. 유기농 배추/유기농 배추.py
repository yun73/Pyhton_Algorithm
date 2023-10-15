'''
유기농 배추

- 지렁이가 있으면 배추 보호 가능
- 상하좌우 인접한 배추들로 이동 가능

- 배추의 군집의 개수를 구하는 문제

- dfs나 bfs 로 군집 조사후 방문 체큰
- 다음번 방문시 체크 된 곳이면 이미 보호 받는 곳
- bfs 돌 때만다 군집개수 한개 추가
'''

T = int(input())
for tc in range(1,T+1):
    M,N,K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cabbage = [0]*K
    ans = 0
    for i in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
        cabbage[i] = (Y,X)
        
    # 각 X,Y 위치에서 bfs 탐색 시작
    for r,c in cabbage:
        # 만약 이미 탐색했다면 그냥 패스
        if visited[r][c]:
            continue
        # 아니라면 bfs 탐색
        
        q = [(r,c)]
        visited[r][c] = 1
        while q:
            i,j = q.pop(0)
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di, j +dj
                if 0<=ni<N and 0<= nj<M and not visited[ni][nj]:
                    # 만약 배추가 아니라면 패스
                    if not arr[ni][nj]:
                        continue
                    visited[ni][nj] = 1
                    q.append((ni,nj))

        # 배추 군집 다 조사했으면
        # 배추지렁이 개수 1개 추가
        ans += 1 

    print(ans)