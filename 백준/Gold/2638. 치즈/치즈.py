# 치즈
# 2변이상 공기와 접촉한 것 한시간 만에 녹아 없어짐
# 모눈 종이 맨 가장자리 치즈 놓이지 않는다
# 외부 공기 부분 -1 로 바꾸자
def check_air(air):
    global cnt
    global visited
    global arr

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited2 = [[0 for _ in range(M)] for _ in range(N)]

    air2 = []
    # 방문한 외부공기라고 표시
    for r,c in air:
        visited[r][c] = 1

    while air:  # 모든 외부 공기영역 탐색할 때 까지
        r, c = air.pop(0)
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:  # 상하좌우 탐색
            nr = r + dr
            nc = c + dc
            # 외부공기 arr 값이 0일 때는 1로 방문했다고만 표시
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                air.append((nr, nc))
                visited[nr][nc] = 1
            # 치즈일 때는 몇번 방문째인지 표시
            # 이미 방문했어도 괜찮음
            elif 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                visited2[nr][nc] += 1
                if visited2[nr][nc] >= 2:  # 외부공간과 2변 이상 닿으면 녹으니까
                    # arr[nr][nc] = 0
                    # 다음에 공기가 되어 탐색할 부분이므로 탐색 리스트에 넣어주자
                    if (nr,nc) not in air2:
                        air2.append((nr, nc))

    for i, j in air2:
        arr[i][j] = 0  # 외부 공기로 바꿔줘
    # for r in range(N):
    #     print(arr[r])
    # print("==========")
    # print(air2)
    return air2


# N x M 의 모눈종이 판
N, M = map(int, input().split())
# 치즈는 1, 없는 부분 0
arr = [list(map(int, input().split())) for _ in range(N)]
# 방문한 곳은 다음에 공기임

# 처음에 탐색 시작할 위치들
cnt = 0
air = [(0, 0)]
check = [[0 for _ in range(M)] for _ in range(N)]
while True:  # 외부공기 리스트에 아무것도 없으면 치즈가 다 녹았다는 거
    air = check_air(air)
    cnt += 1

    # 녹일 치즈가 없으면 종료
    if sum(sum(row) for row in arr) == 0:
        break

print(cnt)
