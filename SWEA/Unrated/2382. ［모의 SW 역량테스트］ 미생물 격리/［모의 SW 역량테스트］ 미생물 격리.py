
# 군집의 이동방향(상: 1, 하: 2, 좌: 3, 우: 4)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]


def renew(site,N):  # 함수 실행될 때 마다 데이터 갱신됨
    # 일단 지역 전체 순회
    # 위치 같은 군집 발견하면
    # 합쳐지면 가장 큰 군집에 나머지 데이터 들을 더해주고
    # 나머지 데이터들을 다 0으로 처리 이동방향도 0은 값 없음
    # 미생물들이 서로 만나면 합쳐지고 이동방향은 젤 큰 군집
    # 데이터 [0,'','']
    for i in range(N):
        for j in range(N):
            k = site[i][j]
            new = ''
            # 미생물이 약품 처리된 칸으로 이동하면
            # //2 연산하고 방향 반대로 *-1 해주면 되는듯
            if k[0] == -1: # 약품처리칸
                if len(k) == 2:  # 미생물이 하나만 있다면
                    mi = site[i][j].pop() # 미생물 하나 뺴주고
                    num = int(mi[:-1])//2 # 개체수 반감
                    go = int(mi[-1])  # 이동방향 전환
                    if go == 1 or go == 3:
                        go += 1
                    elif go == 2 or go == 4:
                        go -= 1
                    if num == 0:  # 개체수 0 되면은
                        pass  # 전체 리스트에 추가 안하고 삭제
                    else:
                        new = str(num) + str(go)
                        site[i][j].append(new)  # 다시 원래 형태로 변환하여 추가

            # 만약 개체수가 0이 되고나서 다른 군집이랑 만나도
            # 개체수가 많은 군집이 메인이 되므로 상관 없음
            if len(k) > 2:  # 미생물이 중복되어 있으면
                num_new = 0  # 합친 개체수
                go = 0  # 갈 이동방향
                max_num = 0
                num_k = len(k)
                for u in range(1, num_k):  # 중복 개체의 정보 합치기, 0번은 칸 정보
                    mi = site[i][j].pop()  # 마지막 얘부터 꺼내와서
                    num_new += int(mi[:-1]) # 각자의 개체수 더해주기
                    if max_num < int(mi[:-1]):
                        max_num = int(mi[:-1])
                        go = int(mi[-1])  # 가장 큰 개체수를 가진 얘의 이동정보 저장
                # 다 합쳐주고 나서 다시 같은 형식으로 정보 저장
                new = str(num_new) + str(go)
                site[i][j].append(new)

    return site


# 매시간마다 미생물 움직이기
def move(site,N):
    # 움직일 때는 한칸에 하나 씩만 있는 상황
    # 각 칸 돌면서 안에 미생물 있으면 진행방향으로 이동시켜주기만 하면 됨
    # 나머지 처리는 renew 함수가 할거야
    # 한시간에 한칸 씩만 움직이면됨
    # 기존 site를 갱신하며 움직이면 애들이 여러번 움직이는 상황이 발생함
    # 그래서 같은 크기의 리스트를 매번 재생성 해서 갱신된 애들 즉 움직인 애들을 넣어준다
    new_site = [[[0] for _ in range(N)] for _ in range(N)]
    # 가장 바깥 부분은 약품 칠해져 있어 -1로 처리하자
    for r in range(N):
        new_site[r][0] = [-1]
        new_site[r][N - 1] = [-1]
        new_site[0][r] = [-1]
        new_site[N - 1][r] = [-1]

    for r in range(N):
        for c in range(N):
            if len(site[r][c]) > 1: # 칸에 미생물이 존재하면
                # 이동할 위치
                mi = site[r][c].pop()  # 미생물은 칸 위치정보 뒤 마지막에 항상 존재
                go = int(mi[-1])
                nr = r + dr[go]
                nc = c + dc[go]
                if 0<=nr<N and 0<=nc<N:
                    # stack = [] # 먼저 들어가 있던 미생물 리스트
                    # if len(site[nr][nc]) > 1: # 해당 칸에 다른 미생물 존재
                    new_site[nr][nc].append(mi)  # 복제 리스트에 이동할 위치에 군집 추가
                    # 그렇게 안하고 append 해버리면 다음번 해당칸을 돌 때 ㅇ
                    # 기존값을 안 꺼내가고 갱신된 값을 가져가 버림
                # 이전 위치의 군집을 pop()으로 뺴내온 후 추가 한 것이므로
                # 추가 처리만 해줘도 무방
    return new_site


T = int(input())
for tc in range(1, T + 1):
    # N : 셀의 개수,  M : 격리시간,  K : 군집개수
    N, M, K = map(int, input().split())
    # 각 행이 미생물 하나의 군집 데이터
    # 세로 위치, 가로 위치, 미생물 수, 이동 방향 순으로 4개의 정수
    micro = [list(map(int, input().split())) for _ in range(K)]
    # 전체 구역 을 매번 갱신 해주며 군집도 위치 갱신?>?
    site = [[[0] for _ in range(N)] for _ in range(N)]
    # 가장 바깥 부분은 약품 칠해져 있어 -1로 처리하자
    for r in range(N):
        site[r][0] = [-1]
        site[r][N - 1] = [-1]
        site[0][r] = [-1]
        site[N - 1][r] = [-1]
    # print(site)
    # 어짜피 우리는 남아있는 미생물의 합을 구하는 거기 때문에
    # 2차원 배열안에 미생물 값과, 이동방향 저장
    for k in micro:
        # print(k)
        info = str(k[2]) + str(k[3])
        site[k[0]][k[1]].append(info)  # 개체수 6 상 이면 61 이런식으로
        # print(site)
        # print(site)
    # 시간마다의 데이터를 처리해야함
    # 격리시간 0 될 때 까지 반복
    # M 시간 돌린 후 종료
    while M > 0:
        site = move(site,N)  # 개체 이동
        site = renew(site,N)  # 군집위치, 정보 갱신
        # print(site)
        M -= 1  # 1시간 동안 일어날 일 다 일어나면 1시간 감소

    # M 시간후 남은 개체수
    total = 0
    # M 시간 후 남은 개체수 조사
    for r in range(N):
        for c in range(N):
            mi = site[r][c]
            if len(mi) > 1:  # 미생물이 있다면
                total += int(mi[1][:-1])  # 미생물의 개체수 정보를 전체 합에 추가

    # M 시간 후 남아 있는 미생물 수의 총 합
    print(f'#{tc} {total}')
