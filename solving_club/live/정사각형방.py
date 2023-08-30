# 상하좌우로 방 이동하는데
# 이동하려는 방 존재, 방에 적힌  정확히 1커야함
# 어디서 시작해야 가장많은 개수의 방을 이동할 수 있어?

# 상하좌우 탐색
di = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(ir,ic):
    global max_visit
    global max_room

    # 큐
    q = []
    q.append((ir,ic))
    # 방문한 방의 개수
    cnt = 1
    while q:
        r,c = q.pop(0)
        for dr,dc in di:
            nr = r + dr
            nc = c + dc
            # 이동위치가 조건을 다 만족하면
            if 0<=nr<N and 0<=nc<N and room[nr][nc] - room[r][c] == 1:
                # 지금까지 방문한 방의 개수 추가
                cnt += 1
                q.append((nr,nc))

    if max_visit < cnt:
        max_visit = cnt
        # 새로운 최대값 찾으면 초기화
        max_room = []
        max_room.append(room[ir][ic])

    elif max_visit == cnt:
        # 같은 경우에는 추가해줘
        max_room.append(room[ir][ic])




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    max_visit = 0
    max_room = []

    # bfs로 방문기록하며 큐에 갈수있는 방을 세면서 간다
    for r in range(N):
        for c in range(N):
            bfs(r,c)

    max_room.sort()

    print(f'#{tc} {max_room[0]} {max_visit}')

    # 이미 방문한 방에 대한 정보를 기록해서 최대값만 찾아가도록?