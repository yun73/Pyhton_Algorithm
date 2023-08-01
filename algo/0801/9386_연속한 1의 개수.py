T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))  # 0011001110
    # arr_0 = list(input().split('0'))

    # 1의 개수를 세기
    count = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        if arr[i] == 1:
            count[i + 1] = count[i] + 1

    # 최대 개수 max_count 구하기
    max_count = 0
    for i in range(len(count)):
        if count[i] > max_count:
            max_count = count[i]

    print(f'#{tc} {max_count}')
