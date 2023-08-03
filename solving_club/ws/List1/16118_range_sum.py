T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))

    max_sum = 1
    min_sum = 1000000
    for i in range(N-M+1):
        sum_M = 0
        for m in range(M):
            sum_M += N_list[i+m]

        if sum_M > max_sum:
            max_sum = sum_M
        if sum_M < min_sum:
            min_sum = sum_M

    result = max_sum - min_sum

    print(f'#{tc} {result}')
