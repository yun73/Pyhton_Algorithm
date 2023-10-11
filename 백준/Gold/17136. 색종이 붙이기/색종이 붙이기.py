'''
색종이 붙이기

- 색종이 : 5종류 5개씩
    - 1x1, 2x2, 3x3, 4x4, 5x5

- 종이 : 10x10
    - 1x1 의 크기로 나눠져 있음
    - 0 : 색종이 있으면 안됨
    - 1 : 색종이로 덮어야 함

- 모든 칸을 붙이는데 필요한 색종이의 최소 개수

1. 일단 1인곳을 찾자
2. 1인 곳에서 bfs 탐색
3. 각 위치마다 5종류의 색종이를 쓸 수 있는지 확인
    - 왼쪽 위에서부터 탐색하니까 항상 탐색 위치는 색종이의 좌측상단 모서리
    - 5*5 부터 채워봐야 하나?
    - 개수 제한이 있으니까 체크리스트 만들기
    - 색종이 채운 곳도 방문표시 해서 넘기기
    - 색종이 덮으면 덮은 곳 0으로 바꾸기
4. 탐색하다 만약 색종이 부족하면 return 하고 다른 경우 탐색

- 아니면 1인 곳을 찾으면서 해당 위치에서 가능한
'''

paper = [list(map(int, input().split())) for _ in range(10)]
used = [5]*5


one = {}
idx = 0
for r in range(10):
    for c in range(10):
        if paper[r][c]:
            one[(r,c)] = idx
            one[idx] = (r,c)
            idx += 1

visited = [0]*idx
# print(one)
min_cnt = int(1e9)
# one 리스트를 백트래킹
# i: 현재 탐색 좌표, end : 채워야 하는 1의 마지막 좌표, now : 지금까지의 색종이의 개수
def bt(i,end,cnt):
    global min_cnt
    # 가지치기
    if cnt >= min_cnt:
        return

    # 종료 조건
    if i == end:
        if min_cnt > cnt:
            min_cnt = cnt
        return

    # 만약 이전 탐색에서 색종이로 같이 채워졌으면 그대로 다음거 탐색
    if visited[i]:
        bt(i+1,end,cnt)
        return

    x, y = one[i][0], one[i][1]
    # 현재 인덱스의 좌표에서 가능한 색종이 탐색
    for n in range(5):
        stack = []
        # 만약 색종이 다 사용했으면 다음거 보자
        if not used[n]:
            continue
        # n이 1인경우는 모두 되니까 백트랙킹
        if n == 0:
            used[n] -= 1
            bt(i+1,end,cnt + 1)
            used[n] += 1
            continue
        # 나머지 경우에 해당 정사각형 범위 만큼 탐색
        for k in range((n+1)**2):
            nx = x + k//(n+1)
            ny = y + k%(n+1)
            # 범위 벗어나면 break
            if not(0 <= nx < 10 and 0 <= ny < 10):
                break
            # 빈 곳이면 break 해당 크기의 정사각형 못써
            if not paper[nx][ny]:
                break
            # 이미 채운 곳이면
            if visited[one[(nx,ny)]]:
                break
            # 채워야 하는 곳이면
            # 정사각형을 만듦에 따라 채워지는 좌표의 인덱스 저장
            stack.append(one[(nx,ny)])
        else:
            # 해당 크기의 정사각형으로 채울 수 있다면 채우고 다음거 가보자
            used[n] -= 1
            for u in stack:
                visited[u] = 1
            bt(i+1,end,cnt+1)
            used[n] += 1
            for u in stack:
                visited[u] = 0

    # 다 돌았는데 색종이 못쓰면 그냥 리턴
    return


if len(one) == 0:
    print(0)
else:
    bt(0,len(visited),0)
    if min_cnt == int(1e9):
        print(-1)
    else:
        print(min_cnt)

