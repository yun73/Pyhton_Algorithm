# 전기버스
# 충전지를 교환하는 방식의 전기버스
# 교체용 충전지가 있는 교환기
# 충전지마다 최대 운행할 수 있는 정류장 수 정해짐

# 충전지 방전되기 전에 교체하며 운행,
# 교체하는 시간 줄이려면 최소한의 교체횟수로 목적지 도달
# 최소한의 교환횟수

def bt(now, goal, cnt):
    global min_cnt

    # 종료조건
    if now >= goal:
        if min_cnt > cnt-1:
            min_cnt = cnt-1
        return
    # 가지치기
    elif cnt-1 >= min_cnt:
        return
    # 재귀 호출
    # 현재 위치에서 갈수있는 거리에 대해서 모두 조사해보자
    else:
        for i in range(battery[now],0,-1):
            bt(now+i, goal, cnt+1)


T = int(input())
for tc in range(1,T+1):
    N, *battery = map(int, input().split())

    # 출발점
    start = 0
    # 종점
    end = N-1

    # 교환횟수 최소값
    min_cnt = 1e9
    # 1번 정류장 부터 값 넣어주고 시작
    bt(start,end, 0)

    print(f'#{tc} {min_cnt}')

