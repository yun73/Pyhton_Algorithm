T = int(input())    # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_val = arr[0]
    min_val = 1000000
    for i in range(1, N):
        if max_val < arr[i]:
            max_val = arr[i]

        if min_val > arr[i]:
            min_val = arr[i]

    ans = max_val - min_val
    print(f'#{tc} {ans}')