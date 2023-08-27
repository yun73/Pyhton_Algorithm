'''
IM 대비 문제 풀기
'''
# 주사위 쌓기
# 보통 주사위 처럼 마주보는 면에 적혀진 숫자으 합이 7 아님
# 쌓을 떄 규칙
# 아래 주사위 윗면 숫자는 위의 주사위 아랫면 숫자와 같아야 함

# 주사위 개수
N = int(input())
# 주어진 주사위
dice = [list(map(int, input().split())) for _ in range(N)]
# [ABCDEF] => A,F 05/ B,D 13/ C,E 24
delete = {0:5, 1:3, 2: 4, 3:1, 4:2, 5:0}
# 다 더했을 떄 가장 큰 옆면
max_side = 0
# 맨 아래 주사위를 정하면 위에 주사위는 알아서 정해진다
# 총 6가지 경우에 대해서만 주사위를 쌓아 올려서 확인하면 됨
for i in range(6): # 첫번쨰 주사위의 아랫면을 i번 인덱스에 있는 숫자라 하자
    side = 0
    now = [1,2,3,4,5,6]
    bottom = dice[0][i]
    top = dice[0][delete[i]]
    # 밑면 윗면 숫자를 제외하자
    now.remove(bottom)
    now.remove(top)
    # 나머지 숫자들 중 최대값을 저장하자
    side += max(now)

    # 다음 위의 주사위로 넘어가서 반복
    for d in range(1,N): # 2번째 주사위부터 전부다 돌기
        # 해당 주사위의 숫자 리스트
        next_now = [1,2,3,4,5,6]
        # 다음층의 주사위 중에 이전 주사위의 윗면에 해당하는 숫자 인덱스 조사하자
        idx = dice[d].index(top)
        # 해당 인덱스로 다음 주사위의 밑면 윗면 갱신
        bottom = top
        top = dice[d][delete[idx]]
        # 이번 주사위의 숫자들중 윗면 아랫면에 해당하는 숫자 지우자
        next_now.remove(bottom)
        next_now.remove(top)
        # 나머지 숫자들 중 최대값을 저장하자
        side += max(next_now)

    if max_side < side:
        max_side = side

print(max_side)
# 윗면 정해지면 짝 제외중 최대값만 이용하면 돼
# 이전 주사위의 윗면을 알아야 해
# 그 다음 주사위는 이전 윗면의 숫자와 아랫면을 알게하면돼
# 아랫면이 정해지면 저절로 윗면 숫자를 알게돼
# 옆면의 값들중 최대값을 이용해
# 이걸 계속 반복해야해
#  1번의 위아래 숫자가 정해지면
# 나머지 주사위 위아래 숫자는 저정로 정해져
# 나머지 숫자들의 합 중 최대값만 구하면 돼
# 현재


