# 두 기차 사이 250 마일
# A는 시속 10마일, B는 시속 15마일
# 파리속도 20마일
# 상대속도 25
# 부딛히는데 10시간
# 10시간 동안 파리 움직임
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # A는 B가 25을 속도로 달려오는 걸로 보임
    relative_speed = A+B
    # A, B 가 부딛힐 떄 까지 걸린 시간
    time = D / relative_speed
    # 파리는 두 기차가 부딛힐 때까지 계속 움직이므로
    # (두기차가 부딛힐 때 까지 걸린 시간) * (파리속력) = 파리가 움직인 거리
    fly_len = time * F

    print(f'#{tc} {fly_len:.10f}')