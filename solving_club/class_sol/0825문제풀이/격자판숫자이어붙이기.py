
# 4x4 의 격자판
# 0~9 까지의 숫자
# 임의의 위치시작, 동서남북 네 방향으로 인접한 격자로 총 6번 이동
# 이동하면서 각 칸에 적혀있는 숫자 이어붙이기 7자리 숫자
# 이동한 칸 다시 가도 됨
# 0으로 시작하는 수도 가능
# 격자판 못 벗어남

# 동서남북 4방향
di = [[0,1],[0,-1],[1,0],[-1,0]]

def bt(r,c,number): # r,c 현재 위치, number 지금까지 이어붙인 문자
    global cnt
    global seven
    # 7번 까지 움직였으면 지금까지 이어붙인거 결과에 넣을 수 있는지 확인하고 개수 추가
    if len(number) == 7:
        if number not in seven: # 7자리 수들 안에 없으면
            cnt += 1  # 개수 하나 추가하고
            seven.add(number) # 7자리 수들에도 넣어줘
        return # 이전 과정으로 돌아가서 다른 길 탐색해봐
    else:
        # 현재 위치에서 갈 수 있는 곳 탐색해봐
        # 동서남북 방향 가보자
        for dr, dc in di:
            nr = r + dr
            nc = c + dc
            if 0<=nr<4 and 0<= nc<4: # 갔던데 또 가도 되니까 범위 안에 있으면 가봐
                # 갈수 있으면
                # 숫자 이어 붙여주고 다음 위치(move+1)에서 탐색해줘
                # number += board[nr][nc] 아래처럼 해주면 초기화 안해줘도 됨
                bt(nr,nc,number + board[nr][nc])


T = int(input())
for tc in range(1, T +1):
    # 격자판 정보 입력
    board = [list(input().split()) for _ in range(4)]

    # 격자판을 이동하면 만들수 있는 서로다른 일곱자리 수들의 모음
    seven = set()
    # 7자리 숫자의 개수
    cnt = 0
    # 모든 행과 열을 순회 -- 임의의 시작점
    for r in range(4):
        for c in range(4):
            # r,c 시작점 숫자 입력
            number = board[r][c]
            bt(r,c,number)

    print(f'#{tc} {cnt}')