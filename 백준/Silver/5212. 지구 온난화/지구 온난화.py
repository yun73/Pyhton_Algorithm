# 지구온난화
# X 는 땅, . 은 바다
# 50년 지나면 인접한 3칸 또는 4칸에 바다가 있는 땅 잠겨버림



R, C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
land = []
for r in range(R):
    for c in range(C):
        if arr[r][c] == 'X':
            land.append((r,c))
sea =[]
min_row = R
max_row = -1
min_col = C
max_col = -1
while land:
    r,c = land.pop(0)
    cnt = 0
    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
        nr, nc = r + dr, c+ dc
        # 범위안에 있고
        if 0<= nr < R and 0<= nc < C :
            # 바다이면
            if arr[nr][nc] == '.':
                cnt += 1

        else: #영역 밖이면 바다
            cnt += 1
    if cnt >= 3:
        sea.append((r,c))
    # 한곳 조사 다 끝났어
    # 바다가 아닐때의 행, 열값 최대 최소 구해야해
    if cnt <= 2:
        if min_row > r:
            min_row = r
        if min_col > c:
            min_col = c
        if max_row < r:
            max_row = r
        if max_col < c:
            max_col = c

while sea:
    r,c = sea.pop(0)
    arr[r][c] = '.'

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        print(arr[i][j], end='')
    print()