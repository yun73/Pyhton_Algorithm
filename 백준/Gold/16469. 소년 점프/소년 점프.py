'''
미로 - RxC
악당 - 상하죄우 칸단위, 안 움직일 수 도 있음
세명이 한 지점에서 모였을 때 걸린시간이 최소가 되는 지점에 마미손이 숨어있다고 확신

시간당 한칸씩 또는 안움직임
각 위치에 들어갈 때 먼저 들어간 사람의 시간대보다 같거나 크면 들어갈 수 있음
방문자의 개수를 체크하는 visited 만들어서
마지막에 3명이 다 방문한 지점이면서 최소시간인 곳을 세주자
기다릴 수 있으므로
먼저 방문한경우는 상관없음
'''
import sys
input = sys.stdin.readline


def bfs(i,q):
    global is_three
    # i 번째 빌런의 첫번째 이동
    # 반환할 다음 탐색지역
    new_b = []
    # 세명이 모두 방문한 지역 나오는 거 체크해줄 인자
    check = 0
    while q:
        x,y = q.pop(0)
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny=x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and not maze[nx][ny] and not visited[i][nx][ny]:
                visited[i][nx][ny] = visited[i][x][y] + 1
                new_b.append((nx,ny))
                # 각 악당이 방문안한곳만 방문하기 때문에 3명이 만나는 곳 체크는 중복 없음
                if visited[0][nx][ny] and visited[1][nx][ny] and visited[2][nx][ny]:
                    is_three += 1
                    check = 1

    return new_b, check


R, C = map(int, input().split())
maze = [list(map(int,input().rstrip())) for _ in range(R)]
billan = [[],[],[]]
visited = [[[0]*C for _ in range(R)]  for _ in range(3)]


for i in range(3):
    x,y = map(int,input().split())
    billan[i].append((x-1, y-1))
    # 시작점 방문 체크
    visited[i][x-1][y-1] = 1

# print(billan)
turn = 0
# 3명된 곳 계산
is_three = 0
while True:
    # 탐색할곳 유무 조사
    cnt = 0
    # 3명 만낫는지 체크
    three_check = 0
    for i in range(3):
        if not billan[i]:
            cnt += 1
            continue
        # bfs 탐색 후 새로운 탐색지역 받기
        billan[i],check_out = bfs(i,billan[i])
        three_check = three_check or check_out
    # 빌런들 움직이는 턴 증가
    turn += 1
    # 3명 다 방문한 곳 나오면 종료
    if three_check:
        break 
    # 3명다 탐색할 곳이 사라지면 종료
    if cnt == 3:
        break

# 3명 된 시점은 turn에 저장되어 있음
# 개수도 저장됨
if is_three:
    print(turn)
    print(is_three)
else:
    print(-1)