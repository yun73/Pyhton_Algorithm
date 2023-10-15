'''
치킨 배달

- 도시 : NxN
    - 빈 칸 : 0
    - 치킨 집 : 2
    - 집 : 1

- 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
    - 도시의 치킨 거리는 모든 집의 치킨 거리의 합

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

- 가장 수익을 많이 낼 수 있는 치킨집 개수 : M

- 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
- 도시의 치킨 거리의 최솟값을 출력

- 집과 가장 가깝게 연결되어있으면 먼 치킨집은 선택했더라도 영향이 없음

- 모든 집에서 bfs 로 치킨집 탐색하면 가장 가까운 곳부터 찍힘
- 최대 집의 개수가 각각의 집에서 가까운 치킨집들 다 합한거보다 작으면
그중에 M 개 선택해야해
- 그럼 차라리 최대 M 개만큼 치킨집 마다 bfs 돌려보며
M 개만큼 도시 선택을 했을때 도시거리 최소를 찾자
'''
import copy
# i: 현재 선택한 치킨집 개수
# M: 최대 M 개의 치킨집 선택 가능
def bt(i,cnt,M,now_visit):
    global min_dis 
    global ch

    # 종료조건
    if cnt == M or i == len(ch):
        # print(sum(now_visit.values()))
        min_dis = min(min_dis, sum(now_visit.values()))
        return
    
    next_visit = now_visit.copy()
    # i 번째 치킨집 선택할지 말지 하고 넘어가기
    # 선택하는 경우
    r,c = ch[i]
    for gr,gc in next_visit.keys():
        next_visit[(gr,gc)]=min(next_visit[(gr,gc)],abs(gr-r)+abs(gc-c))
    bt(i+1,cnt+1,M,next_visit)
    # 선택 안하는 경우
    bt(i+1,cnt,M,now_visit)

    return


N, M = map(int, input().split())
city = [list(map(int,input().split())) for _ in range(N)]

# 치킨집
ch = []
# 집 해당 좌표 방문했는지
visit = {}

for r in range(N):
    for c in range(N):
        if not city[r][c]:
            continue
        if city[r][c] == 1:
            visit[(r,c)] = int(1e9)
            continue
        ch.append((r,c))    
# print(ch)
# print(visit)

min_dis = int(1e9)

bt(0,0,M,visit)
print(min_dis)
