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

- 아니 그냥

'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(mid):
    # 최대와 최소의 차이가 mid 이므로
    # 최소 값인 i 부터 max_num-mid+1 즉 숫자들의 범위가 (i,i+mid) 인 경우에만 탐색해보면 됨
    for i in range(min_num, max_num-mid+1):
        s,e = i, i + mid
        #  만약 시작점과 끝점이 해당 범위 안에 없으면 건너 뛰기
        if not (s<= arr[0][0] <= e and s<= arr[n-1][n-1] <= e):
            continue

        visited = [[0]*n for _ in range(n)]
        q = deque()
        q.append((0,0))
        visited[0][0] = 1
        while q:
            x,y = q.popleft()
            # 종료지점 찾으면 가능한거니까 True 반환
            if (x,y)==(n-1,n-1):
                return True
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx,ny = x + dx, y + dy
                if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and s<= arr[nx][ny] <= e:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
    else:
        return False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# for line in arr:
#     print(*line)

max_num = 0
min_num = 201
for r in range(n):
    for c in range(n):
        if max_num < arr[r][c]:
            max_num = arr[r][c]
        if min_num > arr[r][c]:
            min_num = arr[r][c]

# print(max_num,min_num)
# 최대 최소 차이의 최소 = 0 , 최대 = max_num-min_num
left,right = 0, max_num - min_num
min_mid = 300
while left <= right:
    mid = (left + right)//2
    # print(mid)
    # 만약 이걸로 돌 수 있다면
    if bfs(mid):
        min_mid = min(min_mid,mid)
        # 더 작은 최소 값으로 해보자
        right = mid - 1
    # 안된다면
    else:
        # 더 큰 값으로 해보자
        left = mid + 1

print(min_mid)





