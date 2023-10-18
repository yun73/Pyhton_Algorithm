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


T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    prison = [list(input().strip()) for _ in range(H)]
    print(prison)
    INF = int(1e9)
    # 3차원 visited, 죄수 1,2,3
    visited = [[INF] * W for _ in range(H)]

    # 죄수들의 위치 구하기
    i = 1
    start = []
    for r in range(H):
        for c in range(W):
            if prison[r][c] == '$':
                start.append((i, r, c))
                i += 1
                if i == 3: break
        if i == 3: break


    def escape(start):

        pq = []
        heapq.heappush(pq, (0,start[0][0],start[0][1],start[0][2]))
        heapq.heappush(pq, (0,start[1][0],start[1][1],start[1][2]))

        pass


    escape(start)