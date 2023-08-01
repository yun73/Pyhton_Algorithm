T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(0, N):
        if arr[min_idx] > arr[i]:
            min_idx = i
        if arr[max_idx] <= arr[i]:
            max_idx = i

    ans = max_idx - min_idx
    if ans < 0:
        ans = -ans

    # abs(max_idx - min_idx)
    # max(max_idx, min_idx) - min(max_idx, min_idx)
    print(f'#{tc} {ans}')

