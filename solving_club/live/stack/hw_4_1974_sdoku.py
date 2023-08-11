T = int(input())
for tc in range(1, T + 1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    # 스도쿠 가능하면 1, 아니면 0
    answer = 1
    ans = 1

    for i in range(9):
        stack_row = []
        stack_col = []
        #답 중간점검
        if ans == 0:
            answer = 0
            break

        for j in range(9):
            num_r = puzzle[i][j]
            num_c = puzzle[j][i]
            # 행방향 검증
            if len(stack_row) < 1:
                stack_row.append(num_r)
            else:
                if num_r in stack_row:
                    ans = 0
                    break
                else:
                    stack_row.append(num_r)

            # 열방향 검증
            if len(stack_col) < 1:
                stack_col.append(num_c)
            else:
                if num_c in stack_col:
                    ans = 0
                    break
                else:
                    stack_col.append(num_c)

    # 3x3 배열에서 확인
    for r in range(0, 9 ,3): # 행시작점
        for c in range(0, 9 ,3): # 열시작점
            stack_area = []
            if ans == 0:
                answer = 0
                break

            for i in range(3):
                for j in range(3):
                    num_area = puzzle[r+i][c+j]
                    if len(stack_area) < 1:
                        stack_area.append(num_area)
                    else:
                        if num_area in stack_area:
                            ans = 0
                            break
                        else:
                            stack_area.append(num_area)


    print(f'#{tc} {answer}')