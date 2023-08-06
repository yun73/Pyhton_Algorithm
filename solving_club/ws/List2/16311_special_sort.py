T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # N-1 까지 정렬하면 마지막거는 자동으로
    # 문제에서 10번째 까지만 요구함
    for i in range(10):
        if i % 2 == 1:
            minidx = i
            for j in range(i + 1, N):
                if nums[minidx] > nums[j]:
                    minidx = j
            nums[i], nums[minidx] = nums[minidx], nums[i]

        else:
            maxidx = i
            for j in range(i + 1, N):
                if nums[maxidx] < nums[j]:
                    maxidx = j
            nums[i], nums[maxidx] = nums[maxidx], nums[i]

    print(f'#{tc}', *nums[0:10])
