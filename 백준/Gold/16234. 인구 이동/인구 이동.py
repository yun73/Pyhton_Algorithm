'''
땅 : NxN
각각의 땅에 나라 하나씩 존재
A[r][c] : (r,c) 나라에 살고 있는 인원 수
인접 나라에 경계선, 국경선 정사각형

- 인구이동
    - 두 나라 인구차이 L 명 이상, R 명 이하 >> 국경선 열림
    - 국경선 모두 열리면 인구이동 시작
    - 이동 가능하면 연합
    - 연합 국의 인구수 = 연합 인구수 // 연합 칸 수
    - 연합 해제 후 국경선 닫기

'''
import sys
from collections import deque
input = sys.stdin.readline

def check():
    visited = [[0]*N for _ in range(N)]
    tmp_check_list = {}
    idx = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            visited[r][c] = 1
            q = deque([(r,c)])
            while q:
                x,y = q.popleft()
                for dx,dy in [(0,1),(1,0),(0 ,-1),(-1,0)]:
                    nx,ny = x+dx,y + dy
                    if not (0<=nx<N and 0<=ny<N):
                        continue
                    if visited[nx][ny]:
                        continue
                    if not(L <= abs(arr[nx][ny] - arr[x][y]) <= R):
                        continue
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    tmp_check_list.setdefault(idx,[deque(),0]) # 해당 인덱스로 이어진 나라들 배열 생성
                    tmp_check_list[idx][0].append((nx,ny)) # 배열에 해당되는 나라들 넣기
                    tmp_check_list[idx][1] += arr[nx][ny]

            if idx in tmp_check_list:
                tmp_check_list[idx][1] += arr[r][c]
                tmp_check_list[idx][0].append((r,c))
                idx += 1

    res = False
    if tmp_check_list:
        res = True
    return res,tmp_check_list


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = True
cnt = 0
while result:
    # 인구이동 여부 판단
    result, check_lists = check()
    if not result:
        break
    # 인구이동 시작
    for key in check_lists.keys():
        # 연합나라 개수
        country = len(check_lists[key][0])
        people = check_lists[key][1]
        avg = people // country
        for x,y in check_lists[key][0]:
            arr[x][y] = avg

    cnt += 1

print(cnt)