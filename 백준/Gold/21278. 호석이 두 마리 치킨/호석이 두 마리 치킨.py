'''
호석이 두마리 치킨
도시 안에 2개의 매장
건물 N개, 도로 M개
모든 건물에서 가장 가까운 치킨집까지 왕복하는 최단시가
'''
def bfs(i,j):
    # i와 j 는 다시 돌아오지 않도록 추가하지 말자
    # 가게로부터의 왕복시간 기록
    time = [0] * (N + 1)
    # 큐 생성
    q = []
    # 치킨 가게 시작점들로 넣어놓자
    q.append(i)
    q.append(j)
    # 모든 건물 텀색 다하면 q 값 없어서 종료
    while q:
        # 현재 위치 반환
        now = q.pop(0)
        # 현재 위치와 인접한 건물들로 탐색
        for n in near[now]:
            # 왕복시간도 추가
            # 아직 탐색하지 않은 지역이면
            if time[n] == 0:
                if n != i and n != j:
                    time[n] = time[now] + 2
                    # 연결된 곳 추가
                    q.append(n)
            else:
                if time[n] > time[now] + 2:
                    # 더 작은 왕복 시간 들어오면 갱신해줘
                    time[n] = time[now] + 2
                    # 연결된 곳 추가
                    q.append(n)
                # 이미 들어있는 왕복 시간이 더 작거나 같으면 거기는 탐색하지 않을래

    # 다 돌고나면 치킨집은 다시 0으로 바꿔주고
    time[i], time[j] = 0, 0
    # 접근성 값 계산해서 넘겨줘
    return sum(time)

# N : 건물개수, M : 도로수
N, M = map(int, input().split())
# 인접리스트 생성
near = [[] for _ in range(N + 1)]
# print(near)
for i in range(M):
    A, B = map(int, input().split())
    near[A].append(B)
    near[B].append(A)
# 가장 많이 인접하는 점 찾아주자
many = 0
for i in range(1,N+1):
    if many < len(near[i]):
        many = len(near[i])

# 가장 접근성 좋은 거리 합
nearest = 100000000
# 접근성 거리 좋은 두 건물 리스트
building = []
# 인덱스가 건물 숫자
for i in range(1, N+1):
    # 가장 많이 인접한 건물이면
    # 치킨집 한 곳을 이곳으로 정하고 이 경우 들에 대해서만 조합 조사하자
    if len(near[i]) == many:
        for j in range(1, N+1):
            if j != i:  # 두번째 건물은 자기 자신 제외하고
                # 조합 정해졌으면 접근성 파악하러
                # 해당 지역에서 접근성 최소값
                sub_near = bfs(i, j)

                # 해당 지역 접근성이 저장된 것보다 좋으면
                if nearest > sub_near:
                    # 건물 리스트를 초기화하고
                    building = []
                    nearest = sub_near
                    # 건물정보를 추가해라
                    if (min(i, j), max(i, j)) not in building:
                        building.append((min(i, j), max(i, j)))
                # 접근성 같으면
                elif nearest == sub_near:
                    if (min(i, j), max(i, j)) not in building:
                        building.append((min(i, j), max(i, j)))
                # 접근성 크면 아무것도 안해도 돼

building.sort()
print(*building[0], nearest)
