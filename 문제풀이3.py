# 길 탐색
# 위, 위오대,오, 오아대, 아, 왼아대
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

# 현재 위치에서 갈 수 있는 곳 탐색
# 지도의 너비 높이
w, h = map(int, input().split())
# 지도의 섬과 바다 표시
# 1은 땅, 0은 바다
arr = [list(map(int, input().split())) for _ in range(h)]
# 방문한 지역 1 표시
visited = [[0] * w for _ in range(h)]

# 섬의 개수
cnt = 0

for r in range(h):
    for c in range(w):
        # 현재 위치가 땅이고 방문한 적이 없을 때
        if arr[r][c] == 1 and visited[r][c] == 0:
            visited[r][c] = 1
            stack = []
            while True:
                for d in range(8):
                    # 다음 위치 계산
                    nr = r + dr[d]
                    nc = c + dc[d]
                    # 계산 후에 (nr, nc) 갈 수 있는 곳인지 확인
                    if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == 0 and arr[nr][nc] == 1:
                        # (nr, nc) 위치로 갈 수 있다고 확인
                        # 돌아올 위치를 스택에 저장(현재위치)
                        stack.append((r, c))
                        # 방문 체크
                        visited[nr][nc] = 1
                        # (nr,nc)를 현재위치로 변경
                        r, c = nr, nc
                        # 이전에 탐색하고 있던 r,c
                        # 새로운 위치에서 탐색하기 위해서
                        break
                # 4방향을 모두 다 봤는데 갈 수 있는 곳이 없다.
                else:
                    # 내가 전에 저장해 놨던 최근 위치로돌아가기
                    if stack:
                        r, c = stack.pop()
                    else:
                        cnt+= 1
                        break

print(cnt)

