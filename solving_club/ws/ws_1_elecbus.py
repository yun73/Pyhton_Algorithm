T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    # 최대 이동 거리 K
    # M 정류장 개수
    # N 종점 (0~N) range(0,N+1)
    # 0 번에서 출발해서 3칸 먼저가고 거기에 station 있으면 주유
    # 없으면 2칸가서 있으면 주유
    # 없으면 1칸가서 주유
    # 시작점 0, 종점 N , 이동거리 1,2,..K
    # 종료조건 현재위치 => 시작 += K >= N
    # 충전 횟수 charge
    bus = 0  # 버스현재위치;
    charge = 0  # 충전횟수
    while bus + K < N:
        for i in range(K, 0, -1):
            if (bus + i) in station:
                bus += i
                charge += 1
                break
        else:
            charge = 0
            break

    print(f'#{tc} {charge}')
