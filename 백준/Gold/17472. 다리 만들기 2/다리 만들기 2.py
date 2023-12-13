'''
다리만들기

- 다리
    - 가로, 세로 로만 가능
    - 길이 2 이상
    - 중간에 방향 바뀌면 안됨
- 다리 생성 시 만들어지는 정보
    - 연결된 두 섬 a,b
    - 두 섬을 이어주는 다리 A

> 모든 섬을 연결하는 다리 길이의 최솟값
'''
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
i = 0
# 섬 번호 인덱싱
for r in range(N):
    for c in range(M):
        if Map[r][c] == 0 or visited[r][c]:
            continue
        i += 1
        # 해당 섬 영역 찾아서 바꾸기
        area = [(r,c)]
        while area:
            x,y = area.pop(0)
            Map[x][y] = i
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+ dx, y+dy
                if 0<=nx<N and 0<=ny<M and Map[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    area.append((nx,ny))
# for line in Map:
#     print(*line)

# 섬 마다의 다리연결 정보
INF = int(1e9)
bridge = [[INF]*(i+1) for _ in range(i+1)]

# 가로세로 전부 돌면서 가능한 다리 찾기
for r in range(N):
    land = []
    for c in range(M):
        # 섬 나오면
        if Map[r][c] != 0:
            # 찾은 섬이 1개 있는 경우
            if len(land):
                # 맨 처음 찾은 섬과 같은 경우
                if land[0][0] == Map[r][c]:
                    land[0][1] = c
                    continue
                else:
                    land.append([Map[r][c], c])
                    dis = land[1][1]-land[0][1] - 1
                    if dis >= 2:
                        bridge[land[0][0]][land[1][0]] = min(bridge[land[0][0]][land[1][0]],dis)
                        bridge[land[1][0]][land[0][0]] = min(bridge[land[1][0]][land[0][0]],dis)
                    # 가장 앞에 제거
                    land.pop(0)
                    continue
            else:
                land.append([Map[r][c],c])

for c in range(M):
    land = []
    for r in range(N):
        # 섬 나오면
        if Map[r][c] != 0:
            # 찾은 섬이 1개 있는 경우
            if len(land):
                # 맨 처음 찾은 섬과 같은 경우
                if land[0][0] == Map[r][c]:
                    land[0][1] = r
                    continue
                else:
                    land.append([Map[r][c], r])
                    dis = land[1][1]-land[0][1] - 1
                    if dis >= 2:
                        bridge[land[0][0]][land[1][0]] = min(bridge[land[0][0]][land[1][0]],dis)
                        bridge[land[1][0]][land[0][0]] = min(bridge[land[1][0]][land[0][0]],dis)
                    # 가장 앞에 제거
                    land.pop(0)
                    continue
            else:
                land.append([Map[r][c],r])
#
# for x in range(i+1):
#     for y in range(i+1):
#         if bridge[x][y] == INF:
#             print('.',end=' ')
#             continue
#         print(bridge[x][y],end=' ')
#     print()

# 모든 섬을 연결하기 위한 최소 길이
# 섬은 1~i 번 까지 있음

def find(parent, n):
    if parent[n] == n:
        return n
    return find(parent, parent[n])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        rank[root_y] += 1

def kruskal(graph):
    global i
    edges = []
    parent = [n for n in range(i+1)]
    rank = [0] * (i+1)

    for r in range(1,i+1):
        for c in range(r + 1, i+1):
            if graph[r][c] != INF:
                edges.append((r, c, graph[r][c]))

    edges.sort(key=lambda x: x[2])

    # Kruskal's algorithm
    min_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent, v):
            min_spanning_tree.append(edge)
            union(parent, rank, u, v)

    return min_spanning_tree

# 최소 다리길이 리스트
min_spanning_tree = kruskal(bridge)
# print(i)
# print(min_spanning_tree)

# 총합 계산
total_length = sum(edge[2] for edge in min_spanning_tree)


if len(min_spanning_tree) < i-1:
    print(-1)
else:
    print(total_length)


