# 5x5 2차 배열에 무작위 25개 숫자로 초기화
# 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절대값
import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

# def is_valid(r,c):
#     return 0 <= r < N and 0 <= c < N

for tc in range(1, T + 1):
    N = int(input())
    # 상하좌우(델타)
    # (행의좌표,열의좌표)
    # (r,c)
    # 0 = 상, 1 = 하, 2 = 좌, 3 = 우
    # 상 (-1,0)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열 탐색
    # 행우선으로
    diff_sum = 0
    for r in range(N):
        for c in range(N):
            # print(f'현재 위치: ({r},{c}), 값 : {matrix[r][c]}')
            # 현재 위치에서 상하좌우 차이 절대값 합
            now_diff_sum = 0
            for d in range(4):  # d는 델타 배열의 인덱스
                nr = r + dr[d]
                nc = c + dc[d]
                # 내가 계산한 인덱스가 유효한 범위에 있는지
                # if is_valid(nr,nc):
                if 0 <= nr < N and 0 <= nc < N:
                    diff = matrix[r][c] - matrix[nr][nc]
                    # now_diff_sum += abs(diff)
                    if diff < 0:
                        now_diff_sum -= diff
                    else:
                        now_diff_sum += diff

            diff_sum += now_diff_sum

    print(f'#{tc} {diff_sum}')
    # 상하좌우 탐색
