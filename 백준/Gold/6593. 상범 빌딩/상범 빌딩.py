# 상범 빌딩
# 탕출하는 가장 빠른 길
# 각 변의 길이가 1인 단위정육면체로 이루어짐
# 금으로 이루어져 지나갈 수 없거나, 비어있어서 지나갈 수 있게
# 인접한 6개의 칸 동서남북 상하 로 1분시간 들여 이동가능
# 바깥면도 모두 금으로 막혀있음
import sys
input = sys.stdin.readline

#       북       남       서       동           상       하
di = [[0,-1,0], [0,1,0],[0,0,-1], [0,0,1], [-1,0,0], [1,0,0]]

def bfs(e):
    # e 가 큐
    visited[e[0][0]][e[0][1]][e[0][2]] = 1
    while e:
        i, r, c = e.pop(0)

        for d in range(6):
            ni = i + di[d][0]
            nr = r + di[d][1]
            nc = c + di[d][2]
            if 0<=ni<L and 0<= nr < R and 0<= nc < C and building[ni][nr][nc] != '#':
                if visited[ni][nr][nc] == 0:
                    visited[ni][nr][nc] = visited[i][r][c] + 1
                    e.append((ni,nr,nc))
                # elif visited[ni][nr][nc] > visited[i][r][c] + 1:
                #     visited[ni][nr][nc] = visited[i][r][c] + 1
                #     e.append((ni, nr, nc))
                if building[ni][nr][nc] == 'S':
                    return 1

    return 0


L = R = C = 1
while True:
    # L : 층수, R : 한층의 행, C : 한층의 열
    L, R, C = map(int, input().split())

    if L==0 and R == 0 and C== 0:
        break

    # 빌딩 모양
    # #은 금으로 막혀 지나갈 수 없는 칸, .은 비어있는 칸
    # 시작지점 S
    # 탈출지점 E
    building = [[] for _ in range(L)]# 각 층 정보 주어짐
    for i in range(L):
        building[i] = [input() for _ in range(R)]
        input()

    # 탈출 지점부터 시작지점을 찾자
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start = []
    end = []
    # 시작점과 끝 점 먼저 찾아놓자
    for i in range(L): # 층수
        for r in range(R): # 행수
            for c in range(C): # 열수
                if building[i][r][c] == 'S':
                    start.append((i,r,c))
                elif building[i][r][c] == 'E':
                    end.append((i,r,c))
    # print(start, end)
    # print(building)
    result = bfs(end)
    # print(visited)
    if result:
        print(f'Escaped in {visited[start[0][0]][start[0][1]][start[0][2]]-1} minute(s).')
    else:
        print('Trapped!')

