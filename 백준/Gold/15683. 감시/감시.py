'''

감시

스타트링크 사무실 : N x M
0 : 빈 칸
6 : 벽
1~5 : 카메라 종류

K 개의 카메라
- 1 한쪽 > 4가지
- 2 양쪽 > 2가지
- 3 90도 > 4가지
- 4 180도 > 4가지
- 5 360도 > 1가지
>> 해당 방향에 있는 칸 모두 감시 가능
>> 벽은 통과 못함
>> 회전 가능 90도 방향
>> cctv 는 cctv 통과 가능

>> 빈칸이 최대한 없도록 하자

N,M (1 ≤ N, M ≤ 8)
CCTV의 최대 개수는 8개를 넘지 않는다.

8 * 8 * 5 * 128  =
'''
type_list = {
    1:[[(-1,0)],[(1,0)],[(0,-1)],[(0,1)]],
    2:[[(-1,0),(1,0)],[(0,-1),(0,1)]],
    3:[[(-1,0),(0,1)],[(0,1),(1,0)],[(1,0),(0,-1)],[(0,-1),(-1,0)]],
    4:[[(-1,0),(0,1),(1,0)],[(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)],[(0,-1),(-1,0),(0,1)]],
    5:[[(-1,0),(1,0),(0,-1),(0,1)]],
}


def backtracking(k,visited): # now 는 현재 사각지대의 개수
    global min_cnt

    # 전체 cctv 를 다 확인 하면 최소 개수 확인하고 리턴
    if k == K:
        # 현재 방문한 빈칸 집합으로 만들어 버리고 개수 세기
        now = set(visited)
        min_cnt = min(min_cnt,cnt-len(now))
        return

    # k 번 째 cctv의 종류에 따라 감시 영역 확인하기
    x,y,type = cctv[k]
    for arrow in type_list[type]:
        # 타입마다 90도 회전이 가능해 각각의 경우의 수만큼 돌기
        # 각 경우마다 방문하는 곳 넘겨주기
        visit_this_time = []
        for dx,dy in arrow:
            # 각 방향으로 일직선으로 쭉 감시함
            for dis in range(1,max(N,M)):
                nx,ny = x + dis*dx,y + dis*dy
                # 만약 해당 위치가 범위 안에 없거나 벽이라면
                if not(0<=nx<N and 0<=ny<M) or room[nx][ny] == 6:
                    # cctv 는 그 이상으로 감지 할 수 없으므로 패스
                    break
                # 만약 가능하면 해당 위치 넣어주기
                # 근데 애초에 cctv 는 제외했으니까 빈칸인 곳만
                if room[nx][ny] == 0:
                    visit_this_time.append((nx,ny))

        # 현재 정한 방향으로 다음 cctv 확인하러 가보기
        backtracking(k+1,visited+visit_this_time)




N,M = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = set()

cctv = []

cnt = 0
min_cnt = 65

# CCTV 가 있는 곳 찾기
for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <=5:
            cctv.append((i,j,room[i][j]))
        if room[i][j] == 0:
            cnt += 1

# cctv 의 개수
K = len(cctv)

backtracking(0,[])

print(min_cnt)

