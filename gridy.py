'''
백조의 호수

1. 백조의 위치를 찾으면 백조위치 저장해두고, 물로 바꾸기
2. 물과의 경계부분 다음 탐색 리스트에 추가
3. 하루 지날때 마다
    -빙하 녹는거
        - 녹이면서 다음에 녹을 빙하도
        - 저장된 가장자리 부분들이 전부 녹음
    - 백조 이어졌는지 확인
        - 녹은 가장자리 들에서 bfs 탐색

4. 각 가장자리에 어떤 백조랑 이어져 있는지 저장
5. 가장자리에서 빙하 녹일때 다른 백조 있으면 종료
'''

ddd = {1:2, 2:1, 0:0}

def is_valid(x,y):
    global R, C
    if 0<=x<R and 0<=y<C:
        return True
    else:
        return False

def melt(edge):
    global lake
    # 녹일 곳 다 녹이고
    for r,c, now in edge:
        lake[r][c] = '.'

    new_edge = []
    # 가장자리에서 다음 가장 자리 탐색
    for i,j,now in edge:
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if is_valid(ni, nj) and lake[ni][nj] == 'X' and not visited[ni][nj]:
                visited[ni][nj] = 3
                new_edge.append((ni, nj, now))

    return new_edge

def find(edge):
    # edge 중에서
    while edge:
        i,j,now = q.pop(0)
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if is_valid(ni, nj):
                # 물이면 방문표시 해주고 탐색추가
                if lake[ni][nj] == '.':
                    visited[ni][nj] = visited[x][y]
                    q.append((ni, nj))
                # 가장자리면 방문표시 해주기
                if lake[ni][nj] == 'X':
                    visited[ni][nj] = visited[x][y]
                    new_edge.append((ni, nj))


R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
for r in lake:
    print(r)
# 가장자리
edge = []
# 방문표시
visited = [[0]*C for _ in range(R)]
b = 1
for r in range(R):
    for c in range(C):
        if not visited[r][c] and lake[r][c]=='X':
            for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                nr,nc = r+dr, c+dc
                if is_valid(nr,nc) and lake[nr][nc] != 'X':
                    visited[r][c] = 3
                    edge.append((r,c,3))
                    break
                continue
        if lake[r][c] == 'L':
            visited[r][c] = b
            q = []
            q.append((r,c))
            while q:
                i,j = q.pop(0)
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    ni, nj = i + di, j + dj
                    if is_valid(ni, nj) and not visited[ni][nj]:
                        if lake[ni][nj] != 'X':
                            # 물이면 그냥 다음 탐색에만 추가
                            visited[ni][nj] = b
                            q.append((ni, nj))
                        else:
                            # 빙하면 다음탐색에는 안넣고 가장자리 큐에만
                            visited[ni][nj] = 3
                            edge.append((ni,nj,b))
            b+=1

for r in visited:
    print(r)


# 1일씩 진행
day = 0
while True:
    new_edge = melt(edge)
    result = find(edge)
    day+=1
    print(f'{day}-------------')
    for r in lake:
        print(r)
    for r in visited:
        print(r)
    if result:
        break

print(day)