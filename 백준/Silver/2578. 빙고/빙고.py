'''
IM 대비 문제 풀기
'''
# 빙고
def garo(r,c):
    # 좌우
    dr, dc = 0, -1
    cnt = 1
    for i in [1, -1]:
        nr = r + i * dr
        nc = c + i * dc
        # 탐색범위가 빙고판 내에 있고 0으로 사회자가 부른 값이면
        while 0 <= nr < 5 and 0<= nc < 5 and board[nr][nc] == 0:
            cnt += 1
            nr += i*dr
            nc += i*dc
    if cnt == 5:
        return 1
    else:
        return 0

def sero(r,c):
    # 상하
    dr, dc = -1, 0
    cnt = 1
    for i in [1, -1]:
        nr = r + i * dr
        nc = c + i * dc
        # 탐색범위가 빙고판 내에 있고 0으로 사회자가 부른 값이면
        while 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] == 0:
            cnt += 1
            nr += i * dr
            nc += i * dc
    if cnt == 5:
        return 1
    else:
        return 0
def diag1(r,c):
    # 왼(오) 대각
    dr ,dc = -1, -1
    cnt = 1
    for i in [1, -1]:
        nr = r + i * dr
        nc = c + i * dc
        # 탐색범위가 빙고판 내에 있고 0으로 사회자가 부른 값이면
        while 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] == 0:
            cnt += 1
            nr += i * dr
            nc += i * dc
    if cnt == 5:
        return 1
    else:
        return 0

def diag2(r,c):
    dr, dc = -1, 1
    cnt = 1
    for i in [1, -1]:
        nr = r + i * dr
        nc = c + i * dc
        # 탐색범위가 빙고판 내에 있고 0으로 사회자가 부른 값이면
        while 0 <= nr < 5 and 0 <= nc < 5 and board[nr][nc] == 0:
            cnt += 1
            nr += i * dr
            nc += i * dc
    if cnt == 5:
        return 1
    else:
        return 0


# 철수의 빙고판
board = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 숫자
number = []
for _ in range(5):
    number += list(map(int, input().split()))

bingo = 0
# 빙고된 차례
result = 0
# 빙고가 가능한 경우
# 가로 5개 세로 5개 대각선 2개
# 사회자가 부른 번호 돌면서 일단 0으로 바꿔주자
for n in range(25):
    for r in range(5):
        for c in range(5):
            if board[r][c] == number[n]:
                board[r][c] = 0
                # 가로세로 판별
                bingo += garo(r,c)
                bingo += sero(r,c)
                if r == c: # 왼오 대각선 판별
                    bingo += diag1(r,c)
                if r+c == 4: # 오른쪽 대각선 판별
                    bingo += diag2(r,c)

                if bingo >= 3:
                    result = n+1
                    break
        if bingo >= 3:
            break
    if bingo >= 3:
        break

print(result)
