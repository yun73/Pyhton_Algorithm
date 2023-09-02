# 특이한 자석
# 판마다 4개의 자석
# 각 자석은 8개의 날
# 각 날마다 N극S극의 자성을 가지고 있음
# 자석을 1칸씩 K 번 회전
# 앞에거에 붙어있는 자석 서로 다른 경우만 반대방향으로 1칸 회전
# 회전방향
# 시계방향이 1 로, 반시계 방향이 -1
# 날의 자성 N : 0  S : 1
# 자석정보 빨간색 화살표 위치 날부터 시계방향 순
# 원형 큐 이용해서 마지막 빨간색
def turn():
    pass

T = int(input())
for tc in range(1,T+1):
    # 회전 횟수
    K = int(input())
    # 자석정보
    magnetic = [list(map(int, input().split())) for _ in range(4)]
    # 인접 자석 정보
    near = [[1],[0,2], [1,3], [2]]
    # K 번 입력받아서 자석 돌리자
    for _ in range(K):
        # 돌린 자석들 표시
        used = [0] * 4
        # 돌릴자석, 방향
        mag, di = map(int, input().split())
        mag -=1 # 인덱스 맞춰주기
        used[mag] = 1
        q_mag = []
        q_mag.append((mag,di))
        # 먼저 자석 돌리자
        while q_mag:
            # 처리할 자석 꺼내자
            now, dt = q_mag.pop(0)
            # 해당 자석 돌려놓자
            turn(now, dt)
            # 해당 자석과 붙어 있는 자석들 꺼내자
            for side in near[now]:
                # side 의 맞붙어 있는 자석
                # 맞붙어 있는 자석의 인덱스가 크면 오른쪽 작으면 왼쪽
                if used[side] == 0:  # 아직 안돌린 자석일 때
                    # 사용했다고 표시하고
                    used[side] = 1
                    if side > now: # 오른쪽에 있는거일 때
                        if magnetic[now][2] != magnetic[side][6]:
                            q_mag.append((side, dt * -1))
                        # 같은거면 안돌려도 됨

                    elif side < now: # 왼쪽에 있는거일 때
                        if magnetic[now][6] != magnetic[side][2]:
                            q_mag.append((side, dt * -1))




