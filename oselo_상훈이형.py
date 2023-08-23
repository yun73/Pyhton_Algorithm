def reverse_color(new_i, new_j, new_color):
    arr[new_i][new_j] = new_color
    for d in delta:
        check_i, check_j = new_i, new_j
        change_list = []
        di, dj = d
        check_i += di
        check_j += dj
        if 0 <= check_i < N and 0 <= check_j < N:
            if arr[check_i][check_j] == 0 or arr[check_i][check_j] == new_color:
                continue
            else:
                while 0 <= check_i < N and 0 <= check_j < N:
                    if arr[check_i][check_j] == new_color:
                        for change_color in change_list:
                            arr[change_color[0]][change_color[1]] = new_color
                        break
                    change_list.append([check_i, check_j])
                    check_i += di
                    check_j += dj
    # print(*arr, sep="\n")
    print()


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    arr = [[0] * N for _ in range(N)]
    arr[N // 2 - 1][N // 2 - 1], arr[N // 2][N // 2] = 2, 2
    arr[N // 2 - 1][N // 2], arr[N // 2][N // 2 - 1] = 1, 1
    for _ in range(M):
        ci, cj, color = map(int, input().split())
        cj, ci = ci - 1, cj - 1
        reverse_color(ci, cj, color)

        # 여기는 확인 출력
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    print('W', end=' ')
                elif arr[i][j] == 1:
                    print('B', end=' ')
                else:
                    print('.', end=' ')
            print()
        print('========')


    result_1 = 0
    result_2 = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                result_1 += 1
            elif arr[i][j] == 2:
                result_2 += 1
    print(f"#{tc} {result_1} {result_2}")