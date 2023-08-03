T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a_list = list(map(int, input().split()))
    max_val = a_list[0]
    min_val = 1000000

    for i in range(1, N):
        if a_list[i] > max_val:
            max_val = a_list[i]

        if a_list[i] < min_val:
            min_val = a_list[i]

    result = max_val - min_val

    print(f'#{tc} {result}')
