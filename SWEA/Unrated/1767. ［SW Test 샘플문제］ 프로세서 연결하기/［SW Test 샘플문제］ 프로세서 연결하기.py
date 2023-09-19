# 멕시노스
# NxN 개의 cell
# 1개의 cell에는 1개의 core or 전선
# 가장 자리는 전원 흐름
# 초기 상태 : 전선을 연결하기 전 상태에 멕시노스 정보
'''
# core 와 전원 연결하는 전선은 무조건 직선으로
# 전선 교차 안됨
# 가장자리에 있는 코어는 이미 전원이 연결된 걸로 보자
'''


# 최대한 많은 core에 전원 연결시, 전선 길이의 합의 최소값


# core : 탐색할 코어 리스트
# wire : 지금까지 전선 길이
def bt(k, wire, possible):
    global min_length
    global max_possible
    global core
    global cell

    # 종료조건
    if k == len(core):
        if max_possible < possible:
            max_possible = possible
            min_length = wire
        elif max_possible == possible:
            if min_length > wire:
                min_length = wire
        return

    r, c = core[k]
    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        stack = []
        nr, nc = r + dr, c + dc
        while cell[nr][nc] != -1:
            # 만약 코어나 전선 만나면
            if cell[nr][nc] == 1 or cell[nr][nc] == 2:
                bt(k + 1, wire, possible)
                break
            stack.append((nr, nc))
            nr += dr
            nc += dc
        else:
            for row, col in stack:
                cell[row][col] = 2
            bt(k + 1, wire + len(stack), possible + 1)
            for row, col in stack:
                cell[row][col] = 0



T = int(input())
for tc in range(1, T + 1):
    # 전체 크기
    N = int(input())
    cell = [[-1] * (N + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(N)] + [[-1] * (N + 2)]
    # 일단 먼저 코어의 위치를 받아주자
    core = []
    cnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if cell[r][c] == 1:
                cnt += 1
                if not (r == 1 or r == N or c == 1 or c == N):
                    core.append((r, c))

    min_length = 1000000000
    max_possible = 0
    bt(0, 0, 0)

    print(f'#{tc} {min_length}')
