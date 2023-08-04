T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 당근 개수
    C_list = list(map(int, input().split()))  # 당근의 크기 C를 의미하는 N개의 정수

    max_cnt = 1
    cnt = 1
    for i in range(1, N):
        if C_list[i] > C_list[i - 1]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_cnt}')
