'''
배열에서 이동

- nxn 짜리 배열
- 1,1 >> n,n

- 지나가는 경로의 숫자들 중 최대값과 최소값의 차이가 최소일 때 그 값 출력

- 일단 bfs를 이용한 경로 탐색이다
- 근데 이제 그 경로의 숫자들의 최대, 최소의 차가 최소가 되어야 한다
- 모든 케이스를 다 확인하기에는 시초
- 탐색 방향은 상하좌우, visited는 한번만 해줘도 됨

- 0 <= 최대 - 최소 <= 200
- 생각 1. 이 범위를 이분탐색?

- 생각 2. 가능한 숫자 범위를 이분 탐색
    - 시작점 과 끝점이 1과 5 이면 (1,5) 로 시작
        - 만약 해당 숫자 범위 안에 있는 칸으로만 가서 종료점에 도달한다면
    - 최소값 후보와, 최대 값 후보를 정하자
    - 예를 들어 최소 0 최대 8이면
    최소 값 후보는 0~1 최대값 후보는 5~8

'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs(sr,sc,sub):
    # 해당 경로 까지 가는데 최대 최소 값을 들고가자
    # 그 차이가 mid 같으면
    # 최대 최소 visited
    visited = [[[0,201] for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((sr,sc,arr[sr][sc],arr[sr][sc]))
    visited[sr][sc] = 1
    while q:
        x,y,   = q.popleft()

        for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
            nx,ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:






n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for line in arr:
    print(*line)

max_num = 0
min_num = 201
for r in range(n):
    for c in range(n):
        if max_num < arr[r][c]:
            max_num = arr[r][c]
        if min_num > arr[r][c]:
            min_num = arr[r][c]

print(max_num,min_num)
left,right = min_num, max_num
while left<=right:
    mid = (left + right)//2

    # 만약 이걸로 돌 수 있다면
    # 근데 돌았는데 이거보다 더 작은 걸로 가능한 값이 나오면
    # 그걸 mid로?
    if bfs(0,0,mid):
        # 더 작은 최소 값으로 해보자
        right = mid - 1
    # 안된다면
    else:
        # 더 큰 값으로 해보자
        left = mid+1

print(mid)





