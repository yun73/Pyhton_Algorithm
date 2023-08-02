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



# ---------------------- 강사님 풀이
# 버스 운행하는 함수
def drive(K, N):
    # return == 0 : 충전소가 제대로 배치되어 있지 않다
    # return > 0 : 충전소가 제대로 배치되어 있다

    # 한번에 갈 수 있는 K 까지 가보고
    # 충전기가 없으면 다시 앞으로 한칸 씩 되돌아 오면서
    # 충전기가 있나 확인
    # 이동하기 전 위치로 되돌아오면 충전기가 제대로 배치되어 있지 않으면
    # ==> return 0

    # 되돌아오다가 충전기를 찾으면 K만쿰 또 이동해보고 .. 반복
    last = 0  # 버스가 마지막으로 충전했던 위치
    next = K  # 버스가 최대로 이동한 위치(초기값은 한번 이동한 상태)
    count = 0  # 충전한 횟수

    # 반복하면서 종점까지 이동
    # 버스가 종점에 도착할 때 까지 계속 반복
    while next < N:
        # 버스가 이동한 위치에 충전기가 있나 없나 확인
        while stop[next] == 0:
            # 충전기가 없으면 충전기가 나올 떄까지 앞으로 되돌아 오기
            next -= 1
            # 되돌아 왔는데 이동하기 전 위치로 왔다면
            # 충전기의 위치가 잘못 된 것
            if next == last:
                return 0
        # 충전기가 제대로 설치되어 있다면
        # 마지막 충전위치 갱신하고 다음위치로 이동
        last = next
        next += K
        # 충전기를 만났으니까 충전
        count += 1

    # while 문이 끝나야 도착할 수 있는 코드
    # 정상적으로 충전기가 배치되어 있다.
    # 충전 횟수 return
    return count


T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K : 이동할 수 있는 거리
    # N : 버스가 가야할 거리
    # M : 충전기 개수
    charge = list(map(int, input().split()))  # 충전기 위치 정보
    stop = [0] * N  # 정츄장 리스트
    # stop[i] == 1 : i번 정류장은 충전소가 있는 정류장
    # stop[0] == 0 : i번 정류장은 충전소가 없는 정류장

    for x in charge:
        stop[x] = 1  # 위치 x에는 충전소가 있다고 표시

    answer = drive(K, N)

    print(f'#{tc} {answer}')
