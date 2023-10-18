'''
탈옥

- 평면도 : H x W
    - 빈 공간 : '.'
    - '*' : 벽
    - '#' : 문
    - '$' : 죄수의 위치

- 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최소 개수

- 경우는 총 2가지가 있다
    1. 두 죄수가 각각 최소의 길로 탈출하는 경우
    2. 두 죄수가 같이 최소의 길로 탈출하는 경우

- 각 위치에서 탈출경로를 찾으면서 지금까지 문을 연개수로 한다.
- 만약 탐색하다가 죄수 1,2 가 서로 만나면 죄수번호 3으로 지정하여
같이 탈출할 때의 탈출경로를 찾는다.

'''
import sys, heapq

input = sys.stdin.readline

person = {1: 2, 2: 1}


def is_valid(x, y):
    if 1 <= x <= H and 1 <= y <= W:
        return True
    return False


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    prison = [['.'] * (W + 2)] + [['.'] + list(input().strip()) + ['.'] for _ in range(H)] + [['.'] * (W + 2)]
    # print(prison)

    # 죄수들의 위치 구하기
    i = 1
    start = []
    for r in range(1,H+1):
        for c in range(1,W+1):
            if prison[r][c] == '$':
                prison[r][c] = '.'
                start.append((i, r, c))
                i += 1
                if i == 3: break
        if i == 3: break


    def escape(start):
        INF = int(1e9)
        # 3차원 visited, 죄수 1,2,3
        visited = [[[INF] * (W + 2)] +[[INF] + [INF] * W + [INF] for _ in range(H)] + [[INF] * (W + 2)] for _ in range(4)]
        # 각 죄수의 최단거리
        res = [[] for _ in range(4)]
        pq = []
        heapq.heappush(pq, (0, start[0][0], start[0][1], start[0][2]))
        heapq.heappush(pq, (0, start[1][0], start[1][1], start[1][2]))
        visited[start[0][0]][start[0][1]][start[0][2]] = 0
        visited[start[1][0]][start[1][1]][start[1][2]] = 0

        while pq:
            open, p, x, y = heapq.heappop(pq)

            # 만약 탈출지점이면
            if x == 1 or x == H or y == 1 or y == W:
                res[p].append(open)
                continue

            # 다음위치 확인 및 탐색
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny):
                    # 벽이어서 못가는 경우
                    if prison[nx][ny] == '*':
                        continue
                    # 빈칸인 경우
                    if prison[nx][ny] == '.':
                        next = open

                    # 문이 있는 경우
                    elif prison[nx][ny] == '#':
                        next = open + 1

                    if visited[p][nx][ny] > next:
                        visited[p][nx][ny] = next
                        heapq.heappush(pq, (next, p, nx, ny))

                    # 만약 둘이 만나면
                    if p != 3 and visited[person[p]][nx][ny] != INF:
                        if visited[3][nx][ny] > open + visited[person[p]][nx][ny]:
                            visited[3][nx][ny] = open + visited[person[p]][nx][ny]
                            heapq.heappush(pq, (visited[3][nx][ny], 3, nx, ny))


# 디버깅 코드 ======================================================
#         for i in range(H+2):
#             for j in range(W+2):
#                 if visited[1][i][j] == INF:
#                     print('*', end=' ')
#                     continue
#                 print(visited[1][i][j],end=' ')
#             print()
#
#         print('=========================')
#
#         for i in range(H+2):
#             for j in range(W+2):
#                 if visited[2][i][j] == INF:
#                     print('*', end=' ')
#                     continue
#                 print(visited[2][i][j],end=' ')
#             print()
#
#         print('=========================')
#
#         for i in range(H+2):
#             for j in range(W+2):
#                 if visited[3][i][j] == INF:
#                     print('*', end=' ')
#                     continue
#                 print(visited[3][i][j],end=' ')
#             print()
#
#         print('=========================')
#         print(res)
        # 다 돌면 죄수 1,2 위 최소값의 합 과 죄수 3의 최소값 비교하여 출력
        if res[3]:
            return min(min(res[1]) + min(res[2]), min(res[3]))
        else:
            return min(res[1]) + min(res[2])


    print(escape(start))
