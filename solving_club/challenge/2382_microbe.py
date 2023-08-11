# 군집의 이동방향(상: 1, 하: 2, 좌: 3, 우: 4)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def renew(site):  # 함수 실행될 때 마다 데이터 갱신됨
    # 일단 지역 전체 순회
    # 위치 같은 군집 발견하면
    # 합쳐지면 가장 큰 군집에 나머지 데이터 들을 더해주고
    # 나머지 데이터들을 다 0으로 처리 이동방향도 0은 값 없음
    # 미생물들이 서로 만나면 합쳐지고 이동방향은 젤 큰 군집
    # 데이터 ['','']
    for i in range(N):
        for j in range(N):
            k = site[i][j]
            # 미생물이 약품 처리된 칸으로 이동하면
            # //2 연산하고 방향 반대로 *-1 해주면 되는듯
            if i == 0 or i == N-1:
                if not (int(k[0]) <= 0):
                    num = int(k[0][:-1]) // 2  # 개체수 반감
                    go = int(k[0][-1])
                    if go == 1 or go == 3:
                        go += 1
                    elif go == 2 or go == 4:
                        go -= 1
                    site[i][j] = [str(num) + str(go)]  # 다시 원래 형태로 변환
            elif j == 0 or j == N - 1:
                if not (int(k[0]) <= 0):
                    num = int(k[0][:-1]) // 2  # 개체수 반감
                    go = int(k[0][-1])
                    if go == 1 or go == 3:
                        go += 1
                    elif go == 2 or go == 4:
                        go -= 1
                    site[i][j] = [str(num) + str(go)]  # 다시 원래 형태로 변환

            if not (int(k[0]) <= 0):  # 미생물이 있으면
                du = len(k)  # 중복 개체수
                if du > 1:  # 중복 개체수가 있을 때만 합쳐줌
                    num = 0  # 합친 개체수
                    go = 0  # 갈 이동방향
                    max_num = 0
                    idx = 0  # 합쳐지는 개체의 젤 큰 사람
                    for u in range(du):  # 중복 개체의 정보 합치기
                        num += int(k[u][:-1])  # 각자의 개체수 더해주기
                        if max_num < int(k[u][:-1]):
                            max_num = int(k[u][:-1])
                            max_idx = u
                    go = k[idx][-1]  # 가장 큰 개체수를 가진 얘의 이동정보 저장
                    # 다 합쳐주고 나서 다시 같은 형식으로 정보 저장
                    site[i][j] = [str(num) + str(go)]


    return site


T = int(input())
for tc in range(1, T + 1):
    # N : 셀의 개수,  M : 격리시간,  K : 군집개수
    N, M, K = map(int, input().split())
    # 각 행이 미생물 하나의 군집 데이터
    # 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 4개의 정수
    micro = [list(map(int, input().split())) for _ in range(K)]
    # 전체 구역 을 매번 갱신 해주며 군집도 위치 갱신?>?
    site = [[0] * N for _ in range(N)]
    # 가장 바깥 부분은 약품 칠해져 있어 -1로 처리하자
    for r in range(N):
        site[r][0] = -1
        site[r][N - 1] = -1
        site[0][r] = -1
        site[N - 1][r] = -1

    # 어짜피 우리는 남아있는 미생물의 합을 구하는 거기 때문에
    # 2차원 배열안에 미생물 값과, 이동방향 저장
    for k in K:
        if site[k[0]][k[1]] == 0:
            site[k[0]][k[1]] = []
        site[k[0]][k[1]].append(str(k[2]) + str(k[3]))  # 개체수 6 상 이면 61 이런식으로

    # 시간마다의 데이터를 처리해야함
    # 격리시간 M 일 때부터 반복
    while M > 0:
        M -= 1  # 1시간 동안 일어날 일 다 일어나면 1시간 감소

    # M 시간 후 남아 있는 미생물 수의 총 합
    print(f'#{tc} {total}')
