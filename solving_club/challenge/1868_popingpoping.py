# 파핑파핑 지뢰찾기

# 지뢰 있는 칸 이라면 '파핑파핑!' 게임 종료
# 지뢰 없는 칸이면 변이 맞닿아 있거나, 꼭지점 맞닿아 있는 최대 8칸에 대해
# 몇개의 지뢰가 있는지 0에서 8사이 숫자로 클릭한 칸에 표시
# 숫자가 0이라면 이 근방에 지뢰 없는거 확정
# 그 8칸의 방향도 숫자 표시
# 지뢰 : '*', 지뢰없는 칸 : '.', 클릭한 지뢰 없는 칸 'c'

# 지뢰가 있는 칸을 제외한 다른 모든 칸의 숫자들이 표시되려면 최소 몇번의 클릭?
from collections import deque
di = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]

def bfs(Q):
    global click
    cnt = 0
    while Q:
        q = deque([Q.popleft()])
        # 다음 출발점 불러왔는데 앞에서 체크한게 아니면
        if not click[q[0][0]][q[0][1]]:
            cnt += 1
            while q:
                # 돌다가 탐색 영역에 0인 데가 있으면 카운트 안해줘도 되는 상황
                r,c = q.popleft()
                for dr, dc in di:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        # 지뢰는 탐색하지마
                        if arr[nr][nc] == '*':
                            continue
                        # 숫자일 때는 클릭했다고만 알려줘
                        if arr[nr][nc] > 0:
                            click[nr][nc] = True

                        # 아직 클릭되지 않은 0만 큐에 넣어줘
                        if arr[nr][nc]==0 and not click[nr][nc]:
                            q.append((nr,nc))
                            click[nr][nc] = True
    return cnt

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    click = [[False]*N for _ in range(N)]

    result = 0

    start = deque()
    # 각 위치에서의 지뢰개수 추가
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '*':
                continue
            cnt = 0
            for dr,dc in di:
                nr,nc = r+ dr, c+dc
                if 0<=nr<N and 0<=nc<N and arr[nr][nc] == '*':
                    cnt += 1
            arr[r][c] = cnt
            if cnt == 0:
                start.append((r,c))
    # print(arr)
    result += bfs(start)

    # 클릭해야할 숫자 세기
    for r in range(N):
        for c in range(N):
            # 지뢰는 탐색하지마
            if arr[r][c] == '*':
                continue

            if arr[r][c] > 0 and not click[r][c]:
                result += 1

    print(f'#{tc} {result}')
