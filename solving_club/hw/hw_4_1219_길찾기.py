# A 도시에서 B 도시로 가는길 찾기
# 모든길은 일방통행 >> 유향 그래프
# A, B = 0, 99
# 가는 길 하나라도 있으면 길이 존재

def dfs(adj_l):
    visited = [0] * 100  # 시작은 0 도착은 99 이므로 크기 이렇게 그리고 초기화
    stack = []  # 사용할 스택도 초기화
    # 시작점은 i 라 하면 i는 0부터 시작
    i = 0
    visited[i] = 1  # 처음 출발 위치 0 방문했다고 표시

    while True:
        # 현재 위치 i에서 갈 다음 정점 탐색
        for j in adj_l[i]:  # 한 정점에서 최대로 갈 수 있는 결로는 2개
            # 여기서 j가 나온다면 무조건 경로 찾은거
            if j == 99:
                return 1
            # 만약에 해당 정점이 아직 안간데면
            if visited[j] == 0:
                # 일단 i 지나고 j로 갈거니까
                stack.append(i)
                # 그리고 j 방문했다고 표시
                visited[j] = 1

                # 그리고 현재 위치를 j로 바꿔준다'
                i = j
                break  # i에 대해서 하나의 정점으로만 가야함

        else:
            if stack:  # 아직 스택에 남아있으면
                i = stack.pop()  # 현재위치를 전 위치로 바꾸어서 다시 탐색, 뒷걸음짓
            else:
                break

    return 0


T = 10
for tc in range(1, T + 1):
    adj_l = [[] for _ in range(100)]  # 사용할 경로 리스트 테스트 케이스 마다 초기화
    t, r = map(int, input().split())  # 테스트케이스 번호, 순서쌍 개수
    # 모르겠어서 일단 경로 다 리스트로 받아놓고
    all = list(map(int, input().split()))
    # 받은 개수만큼 돌리면서 사용할 경로 리스트에 추가
    for r in range(r):
        adj_l[all[r*2]].append(all[r*2 + 1])
    print(f'#{tc} {dfs(adj_l)}')
