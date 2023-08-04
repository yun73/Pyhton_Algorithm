T = int(input())
# 원점 + x 축 + y 축 + 사분원 내부*4
for tc in range(1, T + 1):
    N = int(input())
    init_cnt = 1 + N * 4  # 원점과 x축 y 축 위의 점은 기본값으로 미리 계산
    # x,y 의 범위에 원점과 x,y축이 포함되지 않도로 범위 1~N으로 설정
    # 사분원 내의 점의 수
    cnt = 0
    for x in range(1, N):
        for y in range(1, N):
            if x ** 2 + y ** 2 <= N ** 2:
                cnt += 1

    total = init_cnt + cnt * 4

    print(f'#{tc} {total}')
