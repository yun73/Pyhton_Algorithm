'''
로봇 시뮬레이션

- 가로 : A, 세로 : B
- 로봇 : N 개
    - 초기 위치 : x,y
    - NWES 중 하나의 방향을 향해 서있음
- 명령 : M 개'
    - 종류
        - L : 로봇이 향하고 있는 방향을 기준으로 왼쪽으로 90도 회전
        - R: 로봇이 향하고 있는 방향을 기준으로 오른쪽으로 90도 회전
        - F: 로봇이 향하고 있는 방향을 기준으로 앞으로 한 칸 움직
    - 잘못된 명령
        - Robot X crashes into the wall: X번 로봇이 벽에 충돌
        - Robot X crashes into robot Y: X번  Y번 로봇에 충돌

- 내부 범위 : 1<= x <= A and 1<= y <= A

- 명령 상 회전은 왼쪽으로 90 아니면 오른쪽으로 90 이니
    - 시계방향 순인 상우하좌로 하고
        di = ['N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)]

- 입력값이 어떻게 들어오는지 잘 확인
    - 이문제 같은 경우 행과 열중 열이 반전되어 나타남
    - x 가 열값임을 주의
    - 입력 데이터가 돌시에 여러 형태로 들어오는데
    - 어떻게 저장하고 활용할 지 잘 정해야 할 거 같다
'''
di_num = {'N': 0 , 'E' : 1, 'S' : 2, 'W' : 3}
di = [(0,1),(1,0),(0,-1),(-1,0)]

# y 가 행
# x 가 열
# i : 명령을 내릴 로봇, ctype 명령 종류, re 반복 횟수
def command(i,ctype,re):
    # 명령을 실행할 로봇의 현재 위치와 방향
    y,x,go = robots[i]
    # 0 1 2 3 0 1 2 3
    # 왼쪽 90 회전
    if ctype == 'L':
        go = (4 + go - re%4)%4
        robots[i][2] = go
        return 'OK'
    # 오른쪽 90 회전
    elif ctype == 'R':
        go = (go + re) % 4
        robots[i][2] = go
        return 'OK'
    # 지금 저장된 방향으로 이동
    else:
        nx,ny = x,y
        # 현재 로봇의 위치 표시 초기화
        land[y][x] = 0
        # 반복횟수 만큼 이동
        for r in range(re):
            nx += di[go][0]
            ny += di[go][1]
            # 가는 도중에 해당 칸에 다른 로봇 있으면
            if 0<= nx < A and 0<= ny <B:
                if land[ny][nx]:
                    # Robot X crashes into robot Y 출력
                    return f'Robot {i} crashes into robot {land[ny][nx]}'
            else: # 벽에 충돌하면
                # Robot X crashes into the wall 출력
                return f'Robot {i} crashes into the wall'
        # 만약 아무 사고도 안나고 시뮬레이션 성공하면
        else:
            # 해당 위치에 현재 로봇 정보 입력
            robots[i] = [ny,nx,go]
            return 'OK'

# 땅 크기
A, B = map(int, input().split())
# 로봇 개수, 명령 개수
N, M = map(int, input().split())
land = [[0]*A for _ in range(B)]
robots = [0]*(N+1)
# 로봇 위치 및 방향 을 땅에다가 기록
for i in range(1,N+1):
    # i 번 로봇의 위치를 땅에다 입력
    x, y, go = input().split()
    land[int(y)-1][int(x)-1] = i
    robots[i] = [int(y)-1,int(x)-1,di_num[go]]

# 명령 : 명령을 내리는 로봇, 명령종류, 반복 횟수
for _ in range(M):
    i, ctype,re = input().split()
    result = command(int(i),ctype,int(re))
    # 만약 시뮬레이션 결과가 OK 가 아니면
    if result != 'OK':
        print(result)
        # 그대로 종료해라
        break
else:
    print('OK')