
T = int(input())
for tc in range(1,T+1):
    # N : 예약한 사람, M : 굽는 시간 , K : M 초 구웠을 때 만들 수 있는 붕어빵 수
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))

    # 시간 오름차순
    time.sort()

    # 가능한지, 불가능한지
    result = 'Possible'
    # 붕어빵 개수
    fb = 0
    t = 0
    i = 0 # i 가 N 이 되면 possible
    while result == 'Possible' and i < N:
        # 예약한 사람들 차례대로
        while i < N:
            # 에약 시간이 장사 시작 시간
            if time[i] < t + M: # 예약자 시간이 t 초 이후 이지만 더 굽기 전일 때
                if fb - 1 < 0:
                    result = 'Impossible'
                    break
                else:
                    fb -= 1
                    i += 1
            else: # 예약자의 시간이 현재 시간 보다 크면 넘어가서 다음시간 때 판별
                break
        # 2초 뒤로 간다
        t += M
        # 2초 지나면 붕아빵 K 개 생김
        fb += K


    print(f'#{tc} {result}')
