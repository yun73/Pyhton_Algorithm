A = list(range(1, 13))

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    count = 0  # 조건을 만족하는 부분집합의 개수
    for i in range(1 << 12):  # i의 부분집합들을 1 ~ 2^12
        sum_subset = 0
        subset = []
        for j in range(12):  # j가 원소 개수 12 만큼 반복
            if i & (1 << j):  # j 번씩 차례대로 밀면서 부분집합 i에 포함된다면
                subset.append(A[j])  # 부분집합에 원소 추가
                sum_subset += A[j]  # 부분집합 원소들의 함 계산

        if sum_subset == K and len(subset) == N:  # 주어진 조건들을 만족하면
            count += 1  # 개수 +1

    print(f'#{tc} {count}')
