# 백조의 호수
# R,C의 호수 가 얼어있음
# 백조 이동 가로세로로만
# 빙판은 가로세로가 무물에 닿아 있으면 다음 날 녹음
def area(swan):
    global lake
    # i 는 i 번 역역을 의미함
    q = [[],[]]
    for i in range(2):
        sr, sc = swan.pop(0)
        lake[sr][sc] = i
        # 탐색지역 담을 큐
        q[i].append((sr, sc))
        front = -1
        rear = 0
        # 영역 탐색
        while front != rear:
            front += 1
            r,c = q[i][front]
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<R and 0 <= nc <C and lake[nr][nc] == ".":
                    q[i].append((nr,nc))
                    lake[nr][nc] = i
                    rear += 1


R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
# print(lake)
swan = []

# 호수에서 백조의 위치를 찾자
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            swan.append((r, c))

# 먼저 백조의 위치를 기준으로
# 백조가 있는 두 영역을 찾아서 변환 해주기
two_area = area(swan)
min_cnt = 10000
day = 0
while True:
    day += 1