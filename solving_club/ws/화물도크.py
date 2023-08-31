
def bfs(t):
    visit = [0] * N
    visit[t] = 1
    # 큐 생성
    q = []
    q.append((time[t],t))
    # 큐 안에 아무것도 없으면 탐색 끝남
    while q:
        now, t = q.pop(0) # 현재 시간대
        for h in range(t+1, N): # 시간 정렬 되어 있으니까 자기보다 큰 경우에 대해서만 탐색
            if now[1] <= time[h][0]: # 종료 <= 시작 이면 가능
                visit[h] = visit[t] + 1
                q.append((time[h], h))
            else: # 불가능한 경우
                # 그냥 탐색 하지 않아도 됨
                pass
    return max(visit)

T = int(input())
for tc in range(1, T+1):
    # 신청서
    N = int(input())
    # 화물차 개수
    possible = 0
    # 시간대
    time = [0]*N

    # Si, Ti
    for i in range(N):
        s,e = map(int, input().split())
        time[i] = (s,e)
    # 시작시간으로 오름차순 정렬
    time.sort(key = lambda x:x[1])

    for t in range(N):
        cnt = bfs(t)
        if possible < cnt:
            possible = cnt

    print(f'#{tc} {possible}')

T = int(input())
for tc in range(1, T+1):
    # 신청서
    N = int(input())
    # 화물차 개수
    possible = 1
    # 시간대
    time = [0]*N

    # Si, Ti
    for i in range(N):
        s,e = map(int, input().split())
        time[i] = (s,e)
    # 종료시간으로 오름차순 정렬
    time.sort(key = lambda x:x[1])

    n = 1
    end = 0
    while n<N:
        if time[end][1] <= time[n][0]:
            possible += 1
            end = n
        n+=1

    print(f'#{tc} {possible}')