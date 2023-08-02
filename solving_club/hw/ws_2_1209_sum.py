# 100X100 차원 배열
T = 10
for tc in range(1, T + 1):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0

    for r in range(100):
        sum_row = 0  # 각 행의 합
        sum_col = 0  # 각 열의 합
        for c in range(100):
            sum_row += matrix[r][c]  # 행 우선 현재위치를 다 더하기
            sum_col += matrix[c][r]  # 열 우선 현재위치를 다 더하기
        if max_sum < sum_row or max_sum < sum_col:
            # 둘 중 하나라도 최대합 보다 크면 둘 중 큰 값을
            if sum_row >= sum_col:
                max_sum = sum_row
            else:
                max_sum = sum_col
    '''             
    # 행 우선 탐색
    for r in range(100):
        sum_row = 0  # 각 행의 합
        for c in range(100):
            sum_row += matrix[r][c]  # 행 우선 현재위치를 다 더하기
        if max_sum < sum_row:
            max_sum = sum_row

    # 열 우선 탐색
    for r in range(100):
        sum_col = 0  # 각 열열의 합
       for c in range(100):
            sum_col += matrix[c][r]  # 열 우선 현재위치를 다 더하기
        if max_sum < sum_col:
            max_sum = sum_col
    '''

    # 각 대각선의 합

    for x in range(2):
        sum_cro = 0
        for r in range(100):
            sum_cro += matrix[r][r + (100 - 1 - 2 * r) * x]
        if max_sum < sum_cro:
            max_sum = sum_cro

    print(f'#{tc} {max_sum}')
