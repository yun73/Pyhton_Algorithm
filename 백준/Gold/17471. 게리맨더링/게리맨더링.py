# 게리맨더링
# 백준시 N 개의 구역
# 2개의 선거구로 나누자
# 선거구에 최소 1개 잇어야 하고 서로 이어져야돼


def bfs(group):
    global near
    # 해당 그룹 아무데서 시작해서 방문하면 방문했다고 표시
    # 다 돌았는데도 방문 안한곳이 남으면 불가능한 경우 False 반환
    # 다 방문할 수 있으면 True 반환
    # 방문장소 추가
    visited = []
    # 출발장소 방문했다고 표시
    visited.append(group[0])
    # 큐 생성
    Q = []
    # 첫번째 위치 큐에 추가
    Q.append(group[0])
    while Q:
        now = Q.pop(0)
        # 큐에 저장된 구역을 하나 꺼내와
        # 해당 구역에 인접한 구역들을 돌면서 수행
        for i in near[now]:
            # 지금 구역에 속해있는데 중에서, i 번 구역이 아직 방문 안한데라면,
            if i not in visited and i in group:
                Q.append(i)
                visited.append(i)

    if set(group) == set(visited):
        return True
    else:
        return False


# 구역의 개수
N = int(input())
# 구역 인구 정보 1번 부터 N번 구역까지
people = [0] + list(map(int, input().split()))
# 인접 리스트
near = [[] for _ in range(N + 1)]
# N 개 구역의 인접리스트 정보 채우기
for n in range(1, N + 1):
    info = list(map(int, input().split()))
    # 들어온 정보의 첫번째 값은 인접한 지역의 개수
    for i in range(1, info[0] + 1):
        # 정해진 방향 없음
        if info[i] not in near[n]:
            near[n].append(info[i])
        if n not in near[info[i]]:
            near[info[i]].append((n))

# print(near)

# 두 선거구로 나누자
# 최소 한개
# 주어진 구역들 중 1~ N-1 선택
# 하나 선택하면 나머지는 알아서
# 부분 집합 만들기
# 1,2,3,...N 에서 부분집합의 개수는 2^N 개

# 전체 지역번호 리스트
all = set(range(1, N + 1))

# 인구차이 최소값
peo = 100*N-100

for i in range(1 << N):
    subset = []
    for j in range(N):
        if i & (1 << j):
            subset.append(j + 1)
    # 부분집합이 하나 만들어지면
    # 부분집합에 최소 하나 들어갈 경우에
    if subset and len(subset) != N:
        A = set(subset)
        B = all ^ A
        # 두 부분 집합에 대해서 각 집합이 끊기지 않았는 지 확인 해야 함
        if bfs(subset) and bfs(list(B)):
            # 만약 두개다 조건을 만족하면
            # 인구수 계산
            sumA = 0
            sumB = 0
            for a in A:
                sumA += people[a]

            for b in B:
                sumB += people[b]

            if peo > abs(sumA - sumB):
                peo = abs(sumA - sumB)

if peo == 100*N-100: # 두 선거구로 나눌수 없는 경우에는
    print(-1)
else:
    # 두 선거구에 포함된 인구의 차이 최소값
    print(peo)
