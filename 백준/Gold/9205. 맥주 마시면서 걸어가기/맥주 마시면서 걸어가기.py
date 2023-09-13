# 맥주마시면서 걸어가기
# 출발 상근이네
# 맥주 한박스(20개) 들고 출밯
# 목이 마르면 안됨 > 50티어에 한병씩
# 50미터 가려면 그 직전에 마셔야 해
# 편의점 들리면 빈병 버리고 새 맥주병 살 수 있어
# 박스에는 최대 20개
# 편의점 나오고도 한병 마셔야 해
import sys
from collections import deque

def bfs(home_x,home_y, goal_x, goal_y): # 상근이집 x,y , 펜타포트장소 x,y
    # 방문리스트 생성
    visited = set()
    visited.add((home_x, home_y))
    # 큐 생성
    q = deque()
    q.append((0,home_x,home_y))
    while q: # 전부다 탐색할 때 까지
        # 연결 노드도 같이 사용
        idx, r, c = q.popleft()
        for i, nr,nc in node[idx]: # 노드에 연결된 장소들 중
            if (nr,nc) not in visited: # 방문하지 않은 곳이 있으면
                q.append((i,nr,nc)) # 다음 탐색 장소에 넣어주고
                visited.add((nr,nc)) # 방문했다고 넣어줘
            if nr == goal_x and nc == goal_y: # 만약 도착지 나오면 happy
                return "happy"

    # 다 돌았는데도 happy가 안나오면 못찾아서 sad
    return "sad"



T = int(sys.stdin.readline())
for tc in range(1,T+1):
    # 편의점의 개수
    n = int(sys.stdin.readline())
    # n+2 개 줄에 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표
    # x,y 미터
    # 좌표사이 거리 = x좌표사이거리,y좌표사이 거리
    place = []

    for i in range(n+2):
        x,y = map(int, sys.stdin.readline().split())
        place.append((i,x,y))
    # place[0] 번째가 집 place[n+1] 번째가 목적지

    # 두 좌표간 사이의 거리가 무조건 1000이하여야 돼
    # 여러번 편의점 들려도 상관 없음
    # 노드 생성하여 연결해주자
    node = [set() for _ in range(n+2)]
    # print(node)
    for i in range(n+1):
        for j in range(i+1,n+2):
            # 현재 위치와 거리가 1000이하이면
            if abs(place[i][1] - place[j][1]) + abs(place[i][2] - place[j][2]) <= 1000:
                # 무방향 노드이므로 양방향 경로 추가
                node[i].add(place[j])
                node[j].add(place[i])

    home_x,home_y = place[0][1],place[0][2]
    goal_x, goal_y = place[-1][1],place[-1][2]

    result = bfs(home_x,home_y, goal_x, goal_y)
    print(result)


'''
규훈이형 코드

1. 입력들 graph로 연결

2. x + y <= 1000이면 갈 수 있는 거리다

3. abs(현재 x - 도착지 x) + abs(현재 y - 도착지 y) <= 1000이라면 happy

4. 맥주 개수를 굳이 count 해 줄 필요는 없다. - 어차피 편의점 들리면 다시 full로 채워질 것
'''

import sys
input = sys.stdin.readline
T = int(input())

def bfs(sx, sy):
    queue = [(sx, sy)]
    while queue:
        x, y = queue.pop(0)
        # 만약 현재 위치에서 페스티벌까지 갈 수 있다면
        if abs(x - festivalx) + abs(y - festivaly) <= 1000:
            return 'happy'
        else:
            for idx, convenience in enumerate(convenience_stores):
                nx, ny = convenience[0], convenience[1]
                # 만약 편의점이 맥주가 다 떨어지기 전에 존재한다면
                if not visited[idx] and abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visited[idx] = 1

    return 'sad'

for _ in range(T):
    # input
    n = int(input())
    convenience_stores = [0] * n
    homex, homey = map(int, input().split())
    for i in range(n):
        storex, storey = map(int, input().split())
        convenience_stores[i] = (storex, storey)
    festivalx, festivaly = map(int, input().split())

    visited = [0] * (n + 1)
    print(bfs(homex, homey))