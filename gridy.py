'''
로봇

- 이동 : 바라보는 방향 궤도를 따라(동, 서, 남, 북)
- 로봇 이동 제어 명령
    1. GO k: k는 1,2,3 중 하나, 현재 향한 방향으로 k칸 만큼 움직여라
    2. Turn dir: dir은 left or right, 각각 왼쪽 오른쪽으로 90도 회전

- 궤도
    - 0 : 궤도가 있어 로봇이 갈 수 있는 지점
    - 1 : 궤도가 없어 로봇이 갈 수 없는 지점

- 입력
    - 세로길이 : M, 가로길이 : N / 둘 다 100 이하
    - 궤도 서치상태 M줄
    - 출발위치, 바라보는 방향
    - 도착위치 바라보는 방향
- 방향
    - 동쪽 1, 서쪽 2, 남쪽 3, 북쪽 4
    - 0 1 2 3
    - di = [(0,1),(0,-1),(1,0),(-1,0)]
    - di_dict = {0:1, 1:0 3 :4 , 4 :3}

- 구해야 할 것
    - 최단 명령
        - 길이가 짧은지 x
        - 명령 개수가 적어야 함

    - 각 궤도에서 다른 방향으로 가기 위한 명령횟수를 구하고
    - 명령수 가 적은 순으로 우선순위 큐에 넣자
'''
import heapq
di = [(0,1),(0,-1),(1,0),(-1,0)]
di_dict = {0:1, 1:0 , 2 :3 , 3 :2}

def dijk(sr,sc,go,er,ec,eg):
    # 우선순위 큐 생성
    pq = []
    INF = int(1e9)
    # 누적 명령 횟수
    command = [[[INF,0] for _ in range(N)] for _ in range(M)]
    # 시작 지점 초기화
    command[sr][sc][0] = 0
    command[sr][sc][1] = go
    if (sr,sc) == (er,ec):
        if go == eg:
            return 0
        elif go == di_dict[eg]:
            return 2
        else:
            return 1
    heapq.heappush(pq,(0,sr,sc))
    while pq:
        # 우선순위 가장 높은(누적 명령어 가장 낮은) 위치 가져오기
        acc_cmd, r, c = heapq.heappop(pq)
        # 만약 이미 방문했거나 더 큰 누적치가 들어오면
        if command[r][c][0] < acc_cmd:
            continue

        # 현재 위치에서 갈 수 있는 방향 탐색
        for i in range(4):
            for k in range(1,4):
                nr,nc = r + k*di[i][0], c + k*di[i][1]
                # 범위 내이고 궤도가 존재하는 0 이면
                if 0<=nr<M and 0<=nc<N and not arr[nr][nc]:
                    # 누적 명령 계산
                    # 이전 방향과 같은 곳이면
                    new_acc_cmd = acc_cmd+1
                    # 현재 바라보는 방향과 갈 곳의 방향 에 의해 명령 개수 추가
                    if i == command[r][c][1]:
                        new_acc_cmd += 0
                    # 현재 보는 방향과 반대방향일 때
                    elif command[r][c][1] == di_dict[i]:
                        new_acc_cmd += 2
                    else:
                        new_acc_cmd += 1

                    # 만약 종료 값을 찾으면
                    if (nr,nc) == (er,ec):
                        # 현재 바라보는 방향과 갈 곳의 방향 에 의해 명령 개수 추가
                        if eg == i:
                            new_acc_cmd += 0
                        # 현재 보는 방향과 반대방향일 때
                        elif eg == di_dict[i]:
                            new_acc_cmd += 2
                        else:
                            new_acc_cmd += 1

                    # 새로운 갱신 값이 기존 누적값보다 크면 넣지 말자
                    if command[nr][nc][0] <= new_acc_cmd:
                        continue
                    # 새로운 최단 명령누적값 저장
                    command[nr][nc][0] = new_acc_cmd
                    # 보고 있는 방향 저장
                    command[nr][nc][1] = i
                    heapq.heappush(pq,(new_acc_cmd,nr,nc))

                # 범위 밖이거나 중간에 궤도 없는 곳 나오면 해당 방향의 그 이후로는 보지 말자
                else:
                    break # for k

    return command[er][ec][0]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
sr,sc,sg = map(int, input().split())
er,ec,eg = map(int, input().split())
print(dijk(sr-1,sc-1,sg-1,er-1,ec-1,eg-1))


