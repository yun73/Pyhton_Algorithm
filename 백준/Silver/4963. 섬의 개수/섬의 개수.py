# 길 탐색
# 위부터 시계방향
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

# 현재 위치에서 갈 수 있는 곳 탐색
while True:
    # 지도의 너비 높이
    w, h = map(int, input().split())
    # 입력값 0,0 주어지면 종료
    if w ==0 and h == 0:
        break
    # 지도의 섬과 바다 표시
    # 1은 땅, 0은 바다
    arr = [list(map(int, input().split())) for _ in range(h)]

    # 방문한 지역 1 표시
    # visited = [[0 for _ in range(w)] for _ in range(h)]
    # 섬의 개수
    cnt = 0
    # 이거 while 로 입력 값 계속 받아줘야 함
    for r in range(h):
        for c in range(w):
            # 현재 위치가 땅이고 방문한 적이 없을 때
            if arr[r][c] == 1 : # and visited[r][c] == 0
                arr[r][c] = 0
                stack = []
                i = r
                j = c
                while True:
                    for d in range(8):
                        # 다음 위치 계산
                        nr = i + dr[d]
                        nc = j + dc[d]
                        # 계산 후에 (nr, nc) 갈 수 있는 곳인지 확인
                        if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1 : # and visited[nr][nc] == 0
                            # (nr, nc) 위치로 갈 수 있다고 확인
                            # 돌아올 위치를 스택에 저장(현재위치)
                            stack.append((i,j))
                            # 방문 체크
                            arr[nr][nc] = 0
                            # (nr,nc)를 현재위치로 변경
                            i, j = nr, nc
                            # 이전에 탐색하고 있던 r,c
                            # 새로운 위치에서 탐색하기 위해서
                            break
                    # 8방향을 모두 다 봤는데 갈 수 있는 곳이 없다.
                    else:
                        # 내가 전에 저장해 놨던 최근 위치로돌아가기
                        if stack:
                            i, j = stack.pop()
                        else: # 탐색 끝
                            cnt += 1
                            break
    print(cnt)