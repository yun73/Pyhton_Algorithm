T = 10
for t in range(1, T + 1):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착 지점은 2 출발지점 1
    # 도착지점부터 출발 위로만 이동
    # 이동벡터
    # 숫자가 1인 경로를 따라 위쪽으로 가다 오른쪽이나 왼쪽에 1이 나오면 방향 전환환
    # 상 우 좌
    dr = [-1, 0, 0]
    dc = [0, 1, -1]
    # 초기 위치 = 값이 2인곳
    now_r = 99
    now_c = 0
    for col in range(100):
        if ladder[99][col] == 2:
            now_c = col

    while now_r > 0:

        pass




